"""Type A #832 (830-834 window, third leg D->E->A): Reuters x Anthropic
company-sourced aspirational register vs Reuters x Meta enforcement register
(mechanism 730).

Publication-level register replication of mechanism 664 (#717). In a
14-day window (Sep 4-18 2026) Reuters published three Anthropic pieces all
routed through company or company-sympathetic sources: (1) Sep 17, a relay
of Anthropic's own blog post with the company's verb in the headline
("Claude now leads a quarter of work building its next AI models" - 26% of
internal R&D, 90%+ human collaboration, Epoch AI scale; every mitigation
stat company-sourced, no independent adversarial voice, even though the
piece discloses AI building its own successor with "little input from
humans"); (2) Sep 12, Amodei's "We Must Pace the Frontier" essay as a
statesman platform (three-step framework, permanent third-party evaluator
access; the Coxon resignation alarm folded in as reform evidence, not
indictment); (3) Sep 4, the IPO-delay story with the delay normalized in
Reuters' own voice ("such changes are not unusual") and the $2T figure
carried as "one of the largest IPOs ever attempted". In the same 48-hour
window (Sep 17-18) Reuters published two Meta pieces routed through
enforcement sources: (1) Sep 18, the French criminal probe into
smart-glasses sexual harassment (Paris prosecutor's cybercrime unit,
business complaints to data-protection authorities, UK cinema bans, German
criminal complaint) with Meta's commercial success ("market leader", 76%
share, "global hit, selling 7 million units") framed as the problem source;
(2) Sep 17, the German court ruling Meta liable for third-party scam ads
(260 reported violations, up-to-62-day removals, DSA defense rejected,
damages plus ad-revenue disclosure). MANUAL ILLUSTRATIVE: Anthropic arms
+0.45/+0.35/+0.15 (avg +0.32); Meta arms -0.45/-0.35 (avg -0.40);
illustrative delta (Anthropic minus Meta) +0.72. The Reuters-Meta multi-year
content deal (Oct 25 2024) sits on META's side, so the gradient runs
OPPOSITE the naive payer-softening prediction - the null-tie-wire
replication of #717 on a second AI-lab entity in a tighter same-week
window. MANUAL / qualitative only; engine NOT run on the arms per the Aug
28 2026 standing rule; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; verdict directionally_supported_not_proven. NOT a
falsification-family member - register documentation plus replication, not
a uniform-prediction test; falsification ledger holds at 26; no
analysis.json update. Novelty verified pre-commit (zero test_type_a_832
files; no 'Type A #832' in git log; max numeric mechanism_id 729; zero
underscore-form 730 keys by designed keying per #715; block key zero-hit;
all 5 source URLs zero-hit repo-wide; the Sep 13 FT profitability relay was
rejected as a candidate arm because #737 already mapped that URL);
count_stats gate (delta = this file exactly); 830-834 window third leg
D->E->A (anchor patched post-commit per #565) - Sep 18 2026 11:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_832_reuters_anthropic_aspirational_vs_meta_enforcement_register_sep18_11am.py"
MECH_KEY = "reuters_anthropic_company_sourced_aspirational_register_vs_meta_enforcement_register_sep18_2026"
M_ID = 730
ITER = 832
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_730"
NEXT_ID_MARKER = "mechanism" + "_731"
NEXT_ID_NUMERIC = "mechanism_id: 731"
EXPECTED_ORDER = [("A", "832"), ("E", "831"), ("D", "830"), ("C", "829"), ("B", "828")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

EXPECTED_URLS = [
    "https://www.reuters.com/business/anthropic-says-claude-now-leads-quarter-work-building-its-next-ai-models-2026-09-17/",
    "https://www.reuters.com/business/anthropic-ceo-urges-ai-companies-slow-model-development-2026-09-12/",
    "https://www.reuters.com/world/anthropic-ipo-launch-shifts-toward-mid-october-sources-say-2026-09-04/",
    "https://www.reuters.com/technology/french-prosecutors-regulators-step-up-scrutiny-smart-glasses-2026-09-18/",
    "https://www.reuters.com/legal/litigation/german-court-rules-meta-liable-fake-ads-instagram-facebook-2026-09-17/",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "competitor-coverage-research.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\nmethodology:")
    return text[start:end]


def _corpus_ids() -> list:
    ids = []
    for p in (_repo_root() / "profiles").rglob("*.yaml"):
        for m in re.finditer(r"mechanism_id:\s*(\d+)", p.read_text(errors="ignore")):
            ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle: str, roots=("profiles", "tests")) -> list:
    hits = []
    root = _repo_root()
    for r in roots:
        for p in (root / r).rglob("*"):
            if p.is_file() and p.suffix in (".py", ".yaml", ".md", ".json"):
                try:
                    if needle in p.read_text(errors="ignore"):
                        hits.append(str(p.relative_to(root)))
                except OSError:
                    pass
    return hits


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=_repo_root(),
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier: str) -> dict:
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type A #832" in subject:
            mains[sha] = subject
    return mains


def _window(n: int = 40) -> list:
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


def _iteration_log_tail() -> str:
    return (_repo_root() / "iteration-log.md").read_text()[-12000:]


class TestNovelty832:
    """Novelty: deselected pre-commit per the #565 followup convention for the
    main-commit uniqueness pin (the #832 main commit does not exist yet);
    patched green in the anchor followup."""

    def test_single_test_type_a_832_file(self):
        files = list((_repo_root() / "tests").glob("test_type_a_832*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_a_832 file (this one) must exist"
        )

    def test_type_a_832_main_commit_unique_and_anchored(self):
        # Novelty was verified pre-commit by shell greps (zero
        # test_type_a_832 files, no #832 in git log, max numeric
        # mechanism_id 729, zero underscore-form 730 keys, block key
        # zero-hit, all 5 source URLs zero-hit); this test pins that no
        # duplicate #832 main commit ever appears.
        mains = _git_log_mains("Type A #832: reuters x anthropic")
        assert len(mains) == 1, f"exactly one Type A #832 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type A #832 main commit"
        )


class TestRotationCycleGuard832:
    """Rotation: 830-834 window, #830 (D) -> #831 (E) -> #832 (A).

    Deselected pre-commit per the #565 followup convention (the #832 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_830_834_third_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"830-834 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_831(self):
        window = _window()
        assert window[1] == ("E", "831"), (
            f"immediate predecessor must be Type E #831, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per the
        # #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type A #832: reuters x anthropic")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism730Content:
    def test_block_key_exists_in_research_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 832" in block
        assert "rotation_type: A" in block
        assert "2026-09-18" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "Reuters" in block
        assert "Anthropic" in block
        assert "Meta" in block

    def test_three_anthropic_arms_two_meta_arms(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["cross_publication_findings"][MECH_KEY]
        assert len(mech["anthropic_arms"]) == 3
        assert len(mech["meta_arms"]) == 2

    def test_arm_dates_span_sep04_to_sep18(self):
        block = _block()
        for date in ("2026-09-17", "2026-09-12", "2026-09-04", "2026-09-18"):
            assert date in block, date

    def test_source_routing_documented_per_arm(self):
        block = _block()
        for routing in (
            "company_blog_post_relay",
            "ceo_essay_statesman_platform",
            "anonymous_sources_company_adjacent",
            "enforcement_legal_sources",
            "court_ruling_legal_sources",
        ):
            assert routing in block, routing

    def test_claude_autonomy_arm_key_language(self):
        block = _block()
        assert "leads'' 26%" in block or "leads' 26%" in block
        assert "Epoch AI" in block
        assert "1-in-47,000" in block

    def test_amodei_statesman_arm_key_language(self):
        block = _block()
        assert "We Must Pace the Frontier" in block
        assert "third-party evaluator" in block

    def test_ipo_arm_delay_normalized_in_voice(self):
        block = _block()
        assert "such changes are not unusual" in block
        assert "$2 trillion" in block or "$2T" in block

    def test_meta_french_probe_arm_key_language(self):
        block = _block()
        assert "criminal probe" in block
        assert "76%" in block
        assert "7 million units" in block

    def test_meta_german_liability_arm_key_language(self):
        block = _block()
        assert "260 violations" in block
        assert "62 days" in block
        assert "lack-of-knowledge defence" in block

    def test_all_five_source_urls_verbatim(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, url

    def test_no_constructed_reuters_urls(self):
        block = _block()
        urls = re.findall(r"https?://[^\s'\"]+", block)
        for u in urls:
            assert u in EXPECTED_URLS or "reuters.com" not in u, u

    def test_illustrative_tones_and_delta(self):
        block = _block()
        assert "tone_illustrative: 0.45" in block
        assert "tone_illustrative: 0.35" in block
        assert "tone_illustrative: 0.15" in block
        assert "tone_illustrative: -0.45" in block
        assert "tone_illustrative: -0.35" in block
        assert "illustrative_delta_anthropic_minus_meta: 0.72" in block
        assert "anthropic_arm_avg: 0.32" in block
        assert "meta_arm_avg: -0.40" in block

    def test_extends_664_replication_framed(self):
        block = _block()
        assert "EXTENDS mechanism 664" in block
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
        assert "COUNTEREVIDENCE" in mech["counterevidence"][0]

    def test_statistical_discipline_qualitative_only(self):
        block = _block()
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine NOT run" in block
        assert "verdict: directionally_supported_not_proven" in block

    def test_designed_keying_no_underscore_730_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 730 is the only allowed
        # 730 reference.
        block = _block()
        assert "mechanism_730" not in block
        assert "mechanism_id: 730" in block

    def test_research_method_query_sets_and_open(self):
        block = _block()
        assert "5 browser.search query sets" in block
        assert "0 browser.open" in block

    def test_cross_references(self):
        block = _block()
        for ref in ("664", "667", "682"):
            assert f"- {ref}" in block, ref

    def test_distinct_from_prior_717(self):
        # Distinct from #717 (Reuters x OpenAI slowdown-week, mechanism 664):
        # this is the Anthropic replication on a second AI-lab entity, not a
        # re-run of the OpenAI arms.
        block = _block()
        assert "publication-level" in block or "replication" in block
        assert "second AI-lab entity" in block

    def test_profitability_relay_rejected_as_arm(self):
        # The Sep 13 FT profitability relay was mapped by #737; it was
        # rejected as a candidate arm this run, documented in the docstring.
        assert "test_type_a_737" not in _block()
        assert "profitable-second-straight-quarter" not in _block()


class TestSupersessionAndCorpusPost831:
    def test_max_numeric_id_is_730_not_729(self):
        assert max(_corpus_ids()) == 730, (
            "#831 max-729 sweep is superseded by design: the corpus now maxes at 730"
        )

    def test_zero_underscore_731_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 731 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_731_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 731 mechanism keys in the corpus"
        )

    def test_no_second_730_block_key_variant(self):
        # The block key must appear exactly once as a 2-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^  " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_830_zero_underscore_730_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#830 zero-underscore-730 profiles sweep stays green by designed keying"
        )

    def test_830_zero_underscore_730_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#830 zero-underscore-730 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d829_max_729_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 730, (
            "#829 max-729 sweep is superseded by design"
        )

    def test_no_analysis_json_update(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestLedger832:
    def test_twenty_sixth_present_no_twenty_seventh(self):
        corpus = _repo_grep("TWENTY-SIXTH", roots=("profiles",))
        assert len(corpus) >= 1, "TWENTY-SIXTH must be present in profiles/"
        assert _repo_grep("TWENTY-SEVENTH", roots=("profiles",)) == [], (
            "TWENTY-SEVENTH must be absent in profiles/"
        )

    def test_block_states_ledger_holds_at_26(self):
        assert "holds at 26" in _block()

    def test_not_a_falsification_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block


class TestDocSync832:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 42566 |" in readme
        assert "Across 1160 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "42566" in arch and "1160" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog832:
    def test_log_captures_iteration_832(self):
        tail = _iteration_log_tail()
        assert "#832 Type A:" in tail
        assert "11:00 PDT" in tail
        assert "m730" in tail

    def test_log_states_830_834_window(self):
        assert "830-834" in _iteration_log_tail()
