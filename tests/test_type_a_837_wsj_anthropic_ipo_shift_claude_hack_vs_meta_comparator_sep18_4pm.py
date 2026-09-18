"""Type A #837 (835-839 window, third leg D->E->A): WSJ x Anthropic
IPO-shift + Claude-hack register vs WSJ x Meta comparator (mechanism 733).

Same-publication test on the News Corp dual-payer axis. Two fresh Sep 18
2026 WSJ arms on the non-payer Anthropic ($0 AI licensing): (1) the
IPO-to-November business-milestone piece, whose delay is normalized as
strategy (third-quarter financials showing a strong competitive position;
the Coxon warning explicitly back-dated BEFORE the timing decision; $2T /
$100B figures carried as straight investor expectations) - MANUAL
ILLUSTRATIVE +0.25; (2) the Hacktron accountability piece naming Claude as
the attack instrument used to break into OpenAI ("We're just three guys
with Claude and Codex subscriptions"; Claude wrote the exploit code;
employee tokens valid on ChatGPT; Monorepo algorithmic secrets; Anthropic
spokesman declined to comment) - MANUAL ILLUSTRATIVE -0.25 on the
Anthropic-entity reading (OpenAI is the victim, sympathy-adjacent). Two
Meta comparator arms: carried m214 (WSJ Jul 14 "Meta Is Flooding the
Market With Smartglasses", -0.75, un-rescored) and the fresh Sep 9 Dow
Jones Newswires Market Talk relay of the Mizuho Muse-launch note
(constructive, +0.15). Anthropic avg 0.00 vs Meta avg -0.30; illustrative
Anthropic-minus-Meta delta +0.30 - OPPOSITE the naive payer-softening
prediction, the THIRD inverted-gradient replication (m709 Times, m730
Reuters) and the first inside a single publication. MANUAL / qualitative
only; engine NOT run on the arms per the Aug 28 2026 standing rule;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; verdict
directionally_supported_not_proven. NOT a falsification-family member -
register documentation plus replication, not a uniform-prediction test;
falsification ledger holds at 26; no analysis.json update. Novelty
verified pre-commit (zero test_type_a_837 files; no 'Type A #837' in git
log; slugs 8874dffc + b40ba883 zero-hit repo-wide; block-key prefix
zero-hit; Muse Market Talk URL zero-hit; max numeric mechanism_id 732;
zero underscore-form 733 keys by designed keying per #715);
count_stats gate (delta = this file exactly); 835-839 window third leg
D->E->A (anchor patched post-commit per #565) - Sep 18 2026 16:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_837_wsj_anthropic_ipo_shift_claude_hack_vs_meta_comparator_sep18_4pm.py"
MECH_KEY = "wsj_anthropic_ipo_shift_claude_hack_register_vs_meta_comparator_sep18_2026"
M_ID = 733
ITER = 837
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_733"
NEXT_ID_MARKER = "mechanism" + "_734"
NEXT_ID_NUMERIC = "mechanism_id: 734"
EXPECTED_ORDER = [("A", "837"), ("E", "836"), ("D", "835"), ("C", "834"), ("B", "833")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

EXPECTED_URLS = [
    "https://www.wsj.com/tech/ai/anthropic-shifts-planned-ipo-to-november-8874dffc",
    "https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883",
    "https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539",
    "https://www.wsj.com/business/tech-media-telecom-roundup-market-talk-1307ac74",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "news-corp.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  perplexity:")
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
        if "Type A #837" in subject:
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


class TestNovelty837:
    """Novelty: deselected pre-commit per the #565 followup convention for the
    main-commit uniqueness pin (the #837 main commit does not exist yet);
    patched green in the anchor followup."""

    def test_single_test_type_a_837_file(self):
        files = list((_repo_root() / "tests").glob("test_type_a_837*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_a_837 file (this one) must exist"
        )

    def test_type_a_837_main_commit_unique_and_anchored(self):
        # Novelty was verified pre-commit by shell greps (zero
        # test_type_a_837 files, no #837 in git log, max numeric
        # mechanism_id 732, zero underscore-form 733 keys, block-key
        # prefix zero-hit, all 4 source URLs zero-hit); this test pins that no
        # duplicate #837 main commit ever appears.
        mains = _git_log_mains("Type A #837: WSJ x Anthropic")
        assert len(mains) == 1, f"exactly one Type A #837 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type A #837 main commit"
        )


class TestRotationCycleGuard837:
    """Rotation: 835-839 window, #835 (D) -> #836 (E) -> #837 (A).

    Deselected pre-commit per the #565 followup convention (the #837 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_835_839_third_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"835-839 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_836(self):
        window = _window()
        assert window[1] == ("E", "836"), (
            f"immediate predecessor must be Type E #836, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per the
        # #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type A #837: WSJ x Anthropic")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism733Content:
    def test_block_key_exists_in_news_corp(self):
        assert MECH_KEY in _profiles_text()

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 837" in block
        assert "rotation_type" not in block
        assert "rotation: 'Type A'" in block
        assert "2026-09-18" in block

    def test_publication_pair_and_entities(self):
        block = _block()
        assert "Wall Street Journal" in block
        assert "anthropic" in block
        assert "meta" in block

    def test_two_anthropic_arms_two_meta_arms(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["competitor_relationships"][MECH_KEY]
        assert len(mech["anthropic_arms"]) == 2
        assert len(mech["meta_arms"]) == 2

    def test_arm_dates_sep18_sep18_sep09_jul14(self):
        block = _block()
        assert block.count("2026-09-18") >= 3
        assert "2026-09-09" in block
        assert "2026-07-14" in block

    def test_ipo_arm_key_language(self):
        block = _block()
        assert "blockbuster initial public offering" in block
        assert "strong competitive position" in block
        assert "$2 trillion" in block
        assert "$100 billion" in block
        assert "$110 billion in annualized revenue" in block

    def test_ipo_arm_delay_quarantined_off_peg(self):
        block = _block()
        assert "was made before a public warning" in block

    def test_ipo_arm_byline(self):
        block = _block()
        assert "Corrie Driebusch" in block
        assert "Anissa Gardizy" in block
        assert "Kate Clark" in block

    def test_hack_arm_key_language(self):
        block = _block()
        assert "three guys with Claude and Codex subscriptions" in block
        assert "Monorepo" in block
        assert "declined to comment" in block

    def test_hack_arm_entity_split_recorded(self):
        block = _block()
        assert "sympathy-adjacent" in block
        assert "victim" in block

    def test_hack_arm_bug_bounty_bound(self):
        block = _block()
        assert "bug-bounty" in block or "bug bounty" in block
        assert "disclosed to OpenAI" in block

    def test_muse_arm_key_language(self):
        block = _block()
        assert "unveiled Muse" in block
        assert "substantial product cycle" in block
        assert "significant step in that direction" in block
        assert "up 4.5%" in block

    def test_muse_arm_register_note(self):
        block = _block()
        assert "Market Talk" in block
        assert "desk-product" in block

    def test_m214_carried_unrescored(self):
        block = _block()
        assert "mechanism: 214" in block
        assert "carried from m214 by design" in block
        assert "un-rescored" in block

    def test_all_four_source_urls_verbatim(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, url

    def test_no_constructed_wsj_urls(self):
        block = _block()
        urls = re.findall(r"https?://[^\s'\"]+", block)
        for u in urls:
            assert u in EXPECTED_URLS or "wsj.com" not in u, u

    def test_illustrative_tones_and_delta(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["competitor_relationships"][MECH_KEY]
        scorer = mech["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["anthropic_arm_tones"] == [0.25, -0.25]
        assert scorer["anthropic_arm_avg"] == 0.00
        assert scorer["meta_arm_tones"] == [-0.75, 0.15]
        assert scorer["meta_arm_avg"] == -0.30
        assert scorer["illustrative_delta_anthropic_minus_meta"] == 0.30

    def test_dual_payer_inversion_framed(self):
        block = _block()
        assert "OPPOSITE the naive payer-softening prediction" in block
        assert "up to $50M/yr" in block
        assert "THIRD inverted-gradient replication" in block

    def test_extends_wsj_anthropic_arc(self):
        block = _block()
        assert "relation_to_682" in block
        assert "relation_to_689" in block
        assert "relation_to_691" in block
        assert "nine-day range 0.65" in block

    def test_confounder_strengths_ranked_3_3_3(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["competitor_relationships"][MECH_KEY]
        confounders = mech["confounders"]
        assert len(confounders["strong"]) == 3, confounders
        assert len(confounders["moderate"]) == 3, confounders
        assert len(confounders["weak"]) == 3, confounders
        assert "Excerpt-bounded" in confounders["strong"][0]

    def test_counterevidence_three(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["competitor_relationships"][MECH_KEY]
        assert len(mech["counter_evidence"]) == 3
        assert "m682" in mech["counter_evidence"][0]

    def test_statistical_discipline_qualitative_only(self):
        block = _block()
        assert "NOT_CALCULATED - illustrative only" in block
        assert "is_significant: false" in block
        assert "engine: 'NOT run'" in block
        assert "verdict: directionally_supported_not_proven" in block

    def test_designed_keying_no_underscore_733_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 733 is the only allowed
        # 733 reference.
        block = _block()
        # reference. MECH_ID_MARKER is concatenated so this file carries no
        # contiguous underscore-form literal (per the #770 lesson: keeps
        # prior runs' zero-underscore sweeps green).
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 733" in block

    def test_research_method_query_sets_and_open(self):
        block = _block()
        assert "5 browser.search query sets this run" in block
        assert "0 browser.open attempts" in block

    def test_rejected_candidates_documented(self):
        block = _block()
        assert "REJECTED" in block
        assert "The Verge x Anthropic" in block
        assert "The Atlantic x Anthropic" in block
        assert "Guardian x Anthropic" in block
        assert "Accenture" in block

    def test_cross_references(self):
        block = _block()
        for ref in ("relation_to_682", "relation_to_689", "relation_to_691",
                    "relation_to_715", "relation_to_709", "relation_to_730",
                    "relation_to_214"):
            assert ref in block, ref

    def test_distinct_from_prior(self):
        block = _block()
        assert "FIRST dedicated mechanism on the Sep 18 2026 WSJ" in block
        assert "FIRST same-publication WSJ x Anthropic vs WSJ x Meta" in block

    def test_no_analysis_json_update(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestSupersessionAndCorpusPost836:
    def test_max_numeric_id_is_733_not_732(self):
        assert max(_corpus_ids()) == 733, (
            "#836 max-732 sweep is superseded by design: the corpus now maxes at 733"
        )

    def test_zero_underscore_734_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 734 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_734_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 734 mechanism keys in the corpus"
        )

    def test_no_second_733_block_key_variant(self):
        # The block key must appear exactly once as a 2-space YAML key; any
        # second occurrence is a real duplication.
        keys = re.findall(r"^  " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_835_zero_underscore_733_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#835 zero-underscore-733 profiles sweep stays green by designed keying"
        )

    def test_835_zero_underscore_733_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#835 zero-underscore-733 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )


class TestLedger837:
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


class TestDocSync837:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert "| Tests | 42802 |" in readme
        assert "Across 1165 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert "42802" in arch and "1165" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog837:
    def test_log_captures_iteration_837(self):
        tail = _iteration_log_tail()
        assert "#837 Type A:" in tail
        assert "16:00 PDT" in tail
        assert "m733" in tail

    def test_log_states_835_839_window(self):
        assert "835-839" in _iteration_log_tail()
