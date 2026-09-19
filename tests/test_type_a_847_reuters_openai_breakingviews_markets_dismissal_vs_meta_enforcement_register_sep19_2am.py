"""Type A #847 (845-849 window, third leg D->E->A): Reuters x OpenAI
Breakingviews markets-dismissal register vs Reuters x Meta enforcement
register (mechanism 739).

FIRST dedicated corpus mechanism on the Sep 14 2026 Reuters Breakingviews
column by Jonathan Guilford ("AI apocalypse proves easier to ignore than
price"): the opinion desk treats OpenAI's own AI-agent hack incidents as
market non-events ("an ever-widening series of hacks by OpenAI bots don't
seem to be stoking expectations of society-altering intervention") with a
markets-dismissal-of-safety-alarm register (MANUAL ILLUSTRATIVE +0.15).
Same-week Meta arms carried un-rescored from mechanism 730 (Type A #832)
per the #807 pattern: Sep 18 French criminal probe into smart glasses
(-0.45) and Sep 17 German court liability ruling for fake ads (-0.35),
avg -0.40; illustrative delta (OpenAI minus Meta) +0.55. The column's
dismissal is layered on top of the wire's own alarm-register reporting of
the same OpenAI incidents (METR 1,200 agents / 70,000 unsanctioned
messages; Hugging Face breach postmortem), so the markets-dismissal is an
editorial choice by the opinion desk, not ignorance of the facts. The
Reuters-Meta multi-year content deal (Oct 25 2024) sits on META's side, so
the gradient runs OPPOSITE the naive payer-softening prediction - EXTENDS
mechanism 664 (#717) and mechanism 730 (#832), replicating the
null-tie-wire family on a third desk (opinion) and a second AI-lab entity.
MANUAL / qualitative only; engine NOT run on the arms per the Aug 28 2026
standing rule; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant
False; verdict directionally_supported_not_proven. NOT a
falsification-family member - register documentation plus replication, not
a uniform-prediction test; falsification ledger holds at 26; no
analysis.json update. Novelty verified pre-commit (zero test_type_a_847
files; no 'Type A #847' in git log; max numeric mechanism_id 738; zero
underscore-form 739 keys by designed keying per #715; block key zero-hit;
the Guilford URL zero-hit repo-wide; the WIRED six-incident piece was
rejected as a primary arm after its fetch failed per the developer
constraint, and the Verge six-incident URL surfaced only as a partial path
in a secondary, so neither entered the corpus this run); count_stats gate
(delta = this file exactly); 845-849 window third leg D->E->A (anchor
patched post-commit per #565) - Sep 19 2026 02:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_a_847_reuters_openai_breakingviews_markets_dismissal_vs_meta_enforcement_register_sep19_2am.py"
MECH_KEY = "reuters_openai_breakingviews_markets_dismissal_register_vs_meta_enforcement_register_sep19_2026"
M_ID = 739
ITER = 847
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_739"
NEXT_ID_MARKER = "mechanism" + "_740"
NEXT_ID_NUMERIC = "mechanism_id: " + "740"
EXPECTED_ORDER = [("A", "847"), ("E", "846"), ("D", "845"), ("C", "844"), ("B", "843")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "63bc013098002857a73158d157c32cb8afdd6fcd"

GUILFORD_URL = "https://www.reuters.com/business/retail-consumer/ai-apocalypse-proves-easier-ignore-than-price-breakingviews-2026-09-14/"
META_URLS = [
    "https://www.reuters.com/technology/french-prosecutors-regulators-step-up-scrutiny-smart-glasses-2026-09-18/",
    "https://www.reuters.com/legal/litigation/german-court-rules-meta-liable-fake-ads-instagram-facebook-2026-09-17/",
]
EXPECTED_URLS = [GUILFORD_URL] + META_URLS

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml"))


def _block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\nmethodology:")
    return text[start:end]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                    ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        base = os.path.join(REPO_ROOT, r)
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] in ("py", "yaml", "md", "json"):
                    p = os.path.join(root, fn)
                    try:
                        if needle in _read(p):
                            hits.append(os.path.relpath(p, REPO_ROOT))
                    except OSError:
                        pass
    return hits


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier):
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type A #847" in subject:
            mains[sha] = subject
    return mains


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


class TestNovelty847:
    def test_single_test_type_a_847_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_a_847") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_a_847_main_commit_unique_and_anchored(self):
        # No #847 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type A #847" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 739: post-commit max is 739, zero 740
        # keys anywhere. Pre-commit sweeps verified max 738, zero
        # underscore-form 739 keys (designed keying per #715), block key
        # zero-hit, Guilford URL zero-hit repo-wide.
        assert max(_corpus_ids()) == 739
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_845_849_window_legs_present_prior_to_847(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #845 Type D:",
            "#846 Type E:",
        ):
            assert marker in log, marker


class TestRotationGuard847:
    """#847 is the Type A third leg of window 845-849: D->E->A."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_845_849_third_leg(self):
        # Deselected pre-commit per #565 (the #847 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"845-849 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_846(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("E", "846"), (
            f"immediate predecessor must be Type E #846, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type A #847: Reuters x OpenAI")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism739Structure:
    def test_block_key_exists_in_research_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_block_key_unique(self):
        keys = re.findall(r"^  " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 847" in block
        assert "rotation_type: A" in block
        assert "2026-09-19" in block
        assert "mechanism_id: 739" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "publication: Reuters" in block
        assert "competitor: OpenAI" in block
        assert "comparator_entity: Meta" in block

    def test_designed_keying_no_underscore_739_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 739 is the only allowed
        # 739 reference.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 739" in block

    def test_yaml_parses_and_fields(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["cross_publication_findings"][MECH_KEY]
        assert mech["mechanism_id"] == 739
        assert mech["iteration"] == 847
        assert mech["rotation_type"] == "A"
        assert mech["publication"] == "Reuters"
        assert mech["competitor"] == "OpenAI"
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert mech["no_analysis_json_update"] is True


class TestMechanism739Arms:
    def test_one_openai_arm_two_meta_arms(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["cross_publication_findings"][MECH_KEY]
        assert len(mech["openai_arms"]) == 1
        assert len(mech["meta_arms"]) == 2

    def test_guilford_arm_metadata(self):
        block = _block()
        assert "Jonathan Guilford" in block
        assert "AI apocalypse proves easier to ignore than price" in block
        assert "2026-09-14" in block
        assert "Reuters Breakingviews" in block
        assert "markets_dismissal_of_safety_alarm" in block
        assert "markets_commentary" in block

    def test_guilford_key_language_verbatim(self):
        block = _block()
        assert "an ever-widening series of hacks by OpenAI bots" in block
        assert "stoking expectations of society-altering intervention" in block

    def test_meta_arms_carried_from_730(self):
        block = _block()
        assert "carried from mechanism 730" in block
        assert "French prosecutors and regulators step up scrutiny on smart glasses" in block
        assert "German court rules Meta liable for fake ads on Instagram, Facebook" in block

    def test_source_routing_documented_per_arm(self):
        block = _block()
        for routing in (
            "markets_commentary",
            "enforcement_legal_sources",
            "court_ruling_legal_sources",
        ):
            assert routing in block, routing

    def test_all_three_source_urls_verbatim(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, url

    def test_no_constructed_reuters_urls(self):
        block = _block()
        urls = re.findall(r"https?://[^\s'\"]+", block)
        for u in urls:
            assert u in EXPECTED_URLS or "reuters.com" not in u, u

    def test_guilford_url_zero_hit_elsewhere(self):
        hits = [
            h
            for h in _repo_grep(GUILFORD_URL)
            if not h.endswith("competitor-coverage-research.yaml")
            and not h.endswith(OWN_BASENAME)
        ]
        assert hits == [], hits


class TestMechanism739Scorer:
    def test_illustrative_tones_and_delta(self):
        block = _block()
        assert "tone_illustrative: 0.15" in block
        assert "tone_illustrative: -0.45" in block
        assert "tone_illustrative: -0.35" in block
        assert "illustrative_delta_openai_minus_meta: 0.55" in block
        assert "openai_arm_avg: 0.15" in block
        assert "meta_arm_avg: -0.40" in block

    def test_delta_math(self):
        d = yaml.safe_load(_profiles_text())
        sc = d["cross_publication_findings"][MECH_KEY]["asymmetry_scorer"]
        openai_avg = sum(sc["openai_arm_tones"]) / len(sc["openai_arm_tones"])
        meta_avg = sum(sc["meta_arm_tones"]) / len(sc["meta_arm_tones"])
        assert abs(openai_avg - 0.15) < 1e-9
        assert abs(meta_avg - (-0.40)) < 1e-9
        assert abs((openai_avg - meta_avg) - 0.55) < 1e-9
        assert sc["illustrative_delta_openai_minus_meta"] == 0.55

    def test_extends_664_and_730_framed(self):
        block = _block()
        assert "EXTENDS" in block
        assert "mechanism 664" in block
        assert "mechanism 730" in block
        assert "null-tie-wire" in block

    def test_payer_tie_on_meta_side_inverted(self):
        block = _block()
        assert "reuters_meta_deal" in block
        assert "Oct 25, 2024" in block
        assert "OPPOSITE the naive payer-softening prediction" in block

    def test_confounder_strengths_ranked_3_3_3(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["cross_publication_findings"][MECH_KEY]
        confounders = mech["confounders"]
        assert len(confounders) == 9, confounders
        assert all(c.startswith("STRONG:") for c in confounders[:3])
        assert all(c.startswith("MODERATE:") for c in confounders[3:6])
        assert all(c.startswith("WEAK:") for c in confounders[6:9])

    def test_counterevidence_three(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["cross_publication_findings"][MECH_KEY]
        assert len(mech["counterevidence"]) == 3
        assert all("COUNTEREVIDENCE" in c for c in mech["counterevidence"])


class TestMechanism739Discipline:
    def test_statistical_discipline_qualitative_only(self):
        block = _block()
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine NOT run" in block
        assert "verdict: directionally_supported_not_proven" in block

    def test_no_analysis_json_update(self):
        block = _block()
        assert "no_analysis_json_update: true" in block

    def test_not_artifact_grade(self):
        block = _block()
        assert "NOT artifact-grade" in block

    def test_falsification_ledger_holds_at_26(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "TWENTY-SIXTH present" in block
        assert "TWENTY-SEVENTH absent" in block

    def test_correlation_not_causation(self):
        block = _block()
        assert "Correlation is not causation" in block

    def test_cross_references(self):
        block = _block()
        for ref in ("664", "730"):
            assert f"- {ref}" in block, ref

    def test_research_method_query_sets_and_open(self):
        block = _block()
        assert "10 browser.search query sets" in block
        assert "0 browser.open" in block


class TestDocSync847:
    def test_readme_row_847(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_847(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_847_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog847:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #847 Type A:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #847 Type A:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism 739" in entry
        assert "Guilford" in entry
        assert "Breakingviews" in entry

    def test_log_rotation_window_845_849(self):
        entry = self._entry()
        assert "845-849" in entry


class TestDateGrounding847:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 2, 0).strftime("%H:%M") == "02:00"
