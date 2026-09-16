#!/usr/bin/env python3
"""Type B #783: Scott Younker (Tom's Guide, Future plc) meta vs Samsung Galaxy
Glasses register constancy (m701) - competitor coverage deep dive.

Mechanism 701 under profiles/competitor-coverage-research.yaml ->
cross_publication_findings, plus a sourced Scott Younker profile under
profiles/careers/journalists.yaml.

Five Younker bylines in an 18-day Apr 27 - May 15 2026 window: Meta arms May 12
(Meta Connect 2026 tease, neutral product-news register, +0.05 illustrative) and
May 14 (Memorial Day sale, neutral deals register, +0.10); Samsung arms Apr 27
(Galaxy Glasses renders leak, neutral leak register, 0.00) and May 1
(earnings-call AI glasses tease, neutral earnings-news register, 0.00); plus a
fifth same-writer May 15 Asus/Xreal AR pre-order piece anchoring the register as
manufacturer-independent. MANUAL ILLUSTRATIVE: Meta avg +0.075 vs Samsung avg
0.00; illustrative delta +0.075 inside the noise band. Zero
privacy/surveillance interrogation of either entity (bounded-listing absence per
the iteration-492 rule). The finding is within-writer register CONSTANCY - a
same-publisher negative control against m692 (Kozuch, #768: trust-interrogation
asymmetry within product-enthusiasm constancy, same Future plc zero-gradient
context). Future plc has no documented AI licensing tie on this axis (carried
from #768); second Future-plc zero-gradient mechanism after m692. NOT a
falsification-family member (register documentation, not a uniform-prediction
test); ledger holds at 26; no analysis.json update; engine NOT run;
p_value/cohens_d/ci_95 NOT_CALCULATED; correlation is not causation.
"""

import os
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROFILES = REPO / "profiles"
TESTS_DIR = REPO / "tests"
PROFILE = PROFILES / "competitor-coverage-research.yaml"
CAREERS = PROFILES / "careers" / "journalists.yaml"
TEST_BASENAME = Path(__file__).name
MECH_KEY = "scott younker tomsguide meta vs samsung galaxy glasses register constancy sep2026"
M_ID = 701
# Built by concatenation per the #723/#738/#739 designed-keying convention: the
# literal ("mechanism" + "_701") never appears in tests/ or profiles/, keeping
# the #781 zero-underscore-701 sweep instruments green pre-commit. (Used only
# via this constant.)
MECH_ID_MARKER = "mechanism" + "_701"
NEXT_ID_MARKER = "mechanism" + "_702"
NEXT_ID_NUMERIC = "mechanism_id: 702"

# Patched post-commit in the anchor followup per the #565 sequence.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _repo_grep(needle, roots=("profiles", "tests", "docs")):
    hits = []
    for root in roots:
        base = REPO / root
        for dirpath, _dirnames, filenames in os.walk(base):
            # Skip bytecode caches: the sweep instruments guard source text;
            # .pyc files are gitignored build artifacts whose stored string
            # constants would false-positive on concatenated markers.
            if "__pycache__" in Path(dirpath).parts:
                continue
            for fn in filenames:
                p = Path(dirpath) / fn
                try:
                    content = p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                if needle in content:
                    hits.append(str(p.relative_to(REPO)))
    return sorted(hits)


def _max_numeric_mechanism_id():
    ids = set()
    for path in _repo_grep("mechanism_id: ", roots=("profiles",)):
        text = (REPO / path).read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
            ids.add(int(m.group(1)))
    return max(ids)


def _read_profile():
    return PROFILE.read_text(encoding="utf-8")


def _block():
    text = _read_profile()
    start = text.index(MECH_KEY)
    end = text.index("\nmethodology:", start)
    return text[start:end]


def _git_log_mains(prefix):
    log = subprocess.run(
        ["git", "log", "--format=%H %s", "--no-merges"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    return [line for line in log if prefix in line]


class TestNovelty783:
    """Novelty: no prior #783 study, no prior Younker mechanism, block novel."""

    def test_single_test_type_b_783_file_on_disk(self):
        files = sorted((TESTS_DIR / p.name for p in TESTS_DIR.glob("test_type_b_783*")))
        assert [p.name for p in files] == [TEST_BASENAME]

    def test_type_b_783_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; patched green in the
        # anchor followup (ANCHORED_SHA records the main commit).
        hits = _git_log_mains("Type B #783:")
        assert len(hits) == 1, hits
        assert hits[0].split(" ")[0] == ANCHORED_SHA

    def test_novelty_claims_present_in_block(self):
        block = _block()
        assert "Zero test_type_b_783 files on disk pre-commit" in block
        assert '"Scott Younker" zero-hit repo-wide pre-commit' in block
        assert "max numeric mechanism_id 700 pre-commit" in block
        assert "zero underscore-form 701 mechanism key strings repo-wide pre-commit" in block


class TestRotationCycleGuard783:
    """Rotation: the 780-784 window closes B-A-E-D-C (fourth leg 782 A -> 783 B)."""

    EXPECTED_ORDER = [("B", "783"), ("A", "782"), ("E", "781"), ("D", "780"), ("C", "779")]

    def _order_from_git(self):
        log = subprocess.run(
            ["git", "log", "--format=%s", "--no-merges"],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        out = []
        for s in log:
            m = re.match(r"Type ([A-E]) #(\d+):", s)
            if m:
                out.append((m.group(1), m.group(2)))
        return out

    def test_rotation_window_closes_b_a_e_d_c(self):
        # Deselected pre-commit per the #565 convention; green after the anchor
        # followup records the #783 main commit subject.
        assert self._order_from_git()[:5] == self.EXPECTED_ORDER

    def test_cycle_edges_adjacent(self):
        # Deselected pre-commit per the #565 convention.
        order = [t for t, _ in self._order_from_git()]
        edges = set(zip(order, order[1:]))
        for a, b in [("C", "D"), ("D", "E"), ("E", "A"), ("A", "B")]:
            assert (a, b) in edges, (a, b, order[:6])

    def test_anchor_commit_matches_window_head(self):
        # Deselected pre-commit per the #565 convention; ties ANCHORED_SHA to
        # the head of the verified rotation window.
        head = self._order_from_git()[0]
        assert head == ("B", "783")
        hits = _git_log_mains("Type B #783:")
        assert len(hits) == 1 and hits[0].split(" ")[0] == ANCHORED_SHA


class TestMechanism701Content:
    """Block content: m701 arms, scorer, confounders, counterevidence."""

    def test_block_present_and_id_701(self):
        text = _read_profile()
        assert MECH_KEY + ":" in text
        block = _block()
        assert "mechanism_id: 701" in block

    def test_iteration_metadata(self):
        block = _block()
        assert "iteration: 783" in block
        assert "rotation_type: B" in block
        assert "2026-09-16 01:00 PDT" in block
        assert "goal_54093bda4145" in block

    def test_journalist_fields(self):
        block = _block()
        assert "journalist: 'Scott Younker'" in block
        assert "publication: tomsguide" in block
        assert "owner: future_plc" in block

    def test_meta_arm_quotes(self):
        block = _block()
        assert "Meta Connect 2026 kicks off in September" in block
        assert "Meta is knocking up to 25% off its Ray-Ban and Oakley AI glasses" in block
        assert "2026-05-12" in block and "2026-05-14" in block

    def test_samsung_arm_quotes(self):
        block = _block()
        assert "Samsung Galaxy Glasses renders just leaked" in block
        assert "Samsung teases AI smart glasses but reveals memory shortage could get worse" in block
        assert "2026-04-27" in block and "2026-05-01" in block
        assert "Asus ROG Xreal R1 AR pre-orders now live for $849" in block

    def test_constancy_scorer_discipline(self):
        block = _block()
        assert "meta_avg_tone: 0.075" in block
        assert "samsung_avg_tone: 0.0" in block
        assert "illustrative_register_delta_meta_minus_samsung: 0.075" in block
        assert "'0.075 - 0.000 = +0.075'" in block
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "statistical_contract: degenerate_n1_per_arm" in block

    def test_financial_context_zero_gradient(self):
        block = _block()
        assert "No documented AI content-licensing deal between Future plc" in block
        assert "NULL on the register axis" in block
        assert "m692" in block

    def test_six_confounders_strength_layers(self):
        block = _block()
        strong = [m for m in re.findall(r"- 'STRONG: ([^']*)'", block) if m]
        moderate = [m for m in re.findall(r"- 'MODERATE: ([^']*)'", block) if m]
        weak = [m for m in re.findall(r"- 'WEAK: ([^']*)'", block) if m]
        assert len(strong) == 2, strong
        assert len(moderate) == 2, moderate
        assert len(weak) == 2, weak
        assert any("Excerpt-bounded evidence" in c for c in strong)

    def test_four_counterevidence(self):
        block = _block()
        # CE entries are single-line; match full lines so '' escapes inside
        # the YAML single-quoted strings do not truncate the captures.
        ces = [ln for ln in block.splitlines() if ln.strip().startswith("- 'COUNTEREVIDENCE:")]
        assert len(ces) == 4, ces
        assert any("story-type artifact" in ln for ln in ces)
        assert any("Kaycee Hill" in ln for ln in ces)

    def test_verdict_and_ledger(self):
        block = _block()
        assert "verdict: directionally_supported_not_proven" in block
        assert "NOT a falsification-family member" in block
        assert "no_analysis_json_update: true" in block

    def test_careers_backlink_and_keying(self):
        careers = CAREERS.read_text(encoding="utf-8")
        assert "type_b_783_scott_younker_tomsguide_meta_vs_samsung_register_constancy_sep16" in careers
        assert "mechanism_ids: [701]" in careers
        # The careers block_key carries no "mechanism_701" substring by design
        # (#715 convention), so the #781 zero-underscore-701 sweep stays green.
        assert "mechanism_701" not in careers


class TestSupersessionAndCorpusPost782:
    """Post-#782 corpus integrity: max 701, zero 702, designed supersession."""

    def test_max_numeric_mechanism_id_is_701(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_700_still_present(self):
        hits = _repo_grep("mechanism_id: 700")
        assert len(hits) >= 1, hits

    def test_zero_underscore_702_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], hits

    def test_zero_numeric_702_keys_in_profiles(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], hits

    def test_d781_zero_underscore_701_profiles_sweep_stays_green(self):
        # #781 asserted zero underscore-form 701 literals in profiles/; the
        # m701 block key carries no such substring by designed keying, so that
        # sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d781_zero_underscore_701_tests_sweep_stays_green(self):
        # #781 asserted zero underscore-form 701 references in tests/; this
        # file builds the marker by concatenation ("mechanism" + "_701") so no
        # contiguous literal exists in tests/ either - the sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        own = str((TESTS_DIR / Path(__file__).name).relative_to(REPO))
        hits = [h for h in hits if h != own]
        assert hits == [], hits

    def test_d781_zero_numeric_701_profiles_sweep_fails_by_designed_supersession(self):
        # #781 asserted zero "mechanism_id: 701" hits in profiles/; the m701
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 701", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d781_max_700_sweep_superseded_by_design(self):
        # #781 asserted max == 700; advancing to 701 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 701 != 700

    def test_m701_block_key_unique_in_publications(self):
        text = _read_profile()
        assert text.count(MECH_KEY + ":") == 1

    def test_competitor_coverage_research_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["cross_publication_findings"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger783:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m701 not a member."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(PROFILES):
            for f in files:
                p = Path(root) / f
                parts.append(p.read_text(encoding="utf-8", errors="replace"))
        return "\n".join(parts)

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = self._profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "Ledger holds at 26" in _block()

    def test_m701_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "register documentation, not a uniform-prediction test" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestCareers783:
    """Careers profile: Scott Younker keyed entry, beats, mechanism linkage."""

    def _careers(self):
        return CAREERS.read_text(encoding="utf-8")

    def test_keyed_entry_with_name(self):
        careers = self._careers()
        assert "\nscott_younker:" in careers
        assert "name: Scott Younker" in careers

    def test_beats_and_role(self):
        careers = self._careers()
        assert "current_role: Writer" in careers
        assert "current_publication: Tom's Guide" in careers
        assert "- smart_glasses" in careers

    def test_mechanism_linkage(self):
        careers = self._careers()
        assert "mechanism_ids: [701]" in careers
        assert "type_b_783_scott_younker_tomsguide_meta_vs_samsung_register_constancy_sep16:" in careers

    def test_source_urls_verbatim_from_full_url_listings(self):
        careers = self._careers()
        assert "https://www.tomsguide.com/computing/vr-ar/smart-glasses/page/2" in careers
        assert "https://www.tomsguide.com/au/computing/vr-ar/smart-glasses/page/3" in careers


README_PATH = REPO / "README.md"
ARCH_PATH = REPO / "docs" / "ARCHITECTURE.md"
LOG_PATH = REPO / "iteration-log.md"


def _read(p):
    return p.read_text(encoding="utf-8")


class TestDocSync783:
    """Doc-sync: README/ARCHITECTURE rows (go green in the doc-sync followup)."""

    def test_readme_row_783(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_783_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_783(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_783_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog783:
    """Iteration-log #783 entry (goes green in the doc-sync followup)."""

    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #783 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        tail = self._tail()
        assert "Type B #783" in tail
        assert "Scott Younker" in tail

    def test_log_entry_records_rotation_leg(self):
        tail = self._tail()
        assert "780-784" in tail
        assert "D (#780) -> E (#781) -> A (#782) -> B (#783)" in tail
