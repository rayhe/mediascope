"""
Type D #510 - Test & Verify: #509 doc-sync miss repair audit + 506-510
rotation-cycle integrity + window data-mechanism integrity +
asymmetry-scorer engine consistency audit
Sep 4 2026 04:00 PDT - scheduled job_id mediascope-daily-iteration
goal_54093bda4145 rotation 509 C -> 510 D

Failure inventory at run start: risk-window files (506/507/508/509) plus the
structural suite - 4 failed, 237 passed in 179s. All four failures share one
root cause: the #509 Type C run (commit 17e51f9) never performed its
doc-sync pass. Its iteration-log entry has no "Doc sync" section, no
test_type_c_509 row was added to README.md or docs/ARCHITECTURE.md, and the
count headers were left stale at 836 files while 837 existed on disk. The
fix is docs-only: the #509 row (14 pytest-collected tests) is added to both
docs and all three count headers are re-synced to the authoritative
count_stats.py --pytest numbers. See the #510 iteration-log entry for the
verbatim failure output.

New durable guards in THIS file:
- Doc-surface completeness (durable fix for the #509 miss): every test file
  in the 506-510 window must have a per-file row in BOTH README.md and
  docs/ARCHITECTURE.md, and the README row's claimed count must equal the
  file's indented `def test_` count (the repo's documented row convention,
  same regex as the structural per-file check); and every window
  iteration-log entry must carry an explicit "Doc sync" section. The entry
  check is the novel catch: the #509 entry hand-wrote its cumulative file
  count with no Doc sync section at all. Prior guards checked header totals
  and "lists all files" but never verified per-window-file row presence or
  the sync step itself, so a skipped doc-sync only surfaced via the header
  totals a full hour later. This guard fails the hour the sync is skipped.
- Rotation-cycle integrity 506-510: line-anchored headings
  (^#N Type X:) must appear newest-first as 510 D, 509 C, 508 B, 507 A,
  506 E (durable rule from #495b - entry prose quotes heading literals, so
  unanchored substring search is banned).
- Git-order consistency: the five "Type #" commits preceding this run are
  509, 508, 507, 506, 505 in descending newest-first order (commit-layer
  mirror of the log rotation check).
- Window data-mechanism integrity: the data facts each window run claimed
  exist in the YAML tree - mechanism_507 under the-verge.yaml
  competitor_relationships.openai; mechanism_509 under
  competitor-entities.yaml entities.anthropic; the 508 competitor_coverage
  block on the Kurt Wagner entry in profiles/careers/journalists.yaml; the
  24th podcast verification cycle section for #506 in podcast-sentiment.md.
- Asymmetry-scorer engine consistency audit (repo-wide): for every
  asymmetry_scorer_result block in profiles/**, is_significant must equal
  (p_value < 0.05) - the engine's documented rule in
  mediascope/score/asymmetry.py - asymmetry_score must equal
  target_avg - peer_avg, recorded averages must equal the mean of their
  recorded tone lists, and 95% CI bounds must be well-ordered, wherever the
  fields are numeric. 28 blocks audited at write time, 0 violations. This
  is the Type D statistical-meaningfulness verification for this run: it
  cannot bless manual illustrative tones, but it guarantees the engine's
  recorded outputs are internally consistent and the significance flag
  cannot silently drift from the p-value.

Statistical discipline: metadata and repo-integrity only; no tone scores,
no p_value, no significance claimed. All scorer numbers asserted here are
recorded engine outputs, not new analyses. correlation_not_causation is
untouched by this run.

Goal and job IDs: goal_54093bda4145 mediascope-daily-iteration iteration 510 Type D 2026-09-04 04:00 PDT
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "iteration-log.md"
PROFILES = REPO / "profiles"
TESTS_DIR = REPO / "tests"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
PODCAST = REPO / "podcast-sentiment.md"

WINDOW_FILES = [
    "test_type_e_506_podcast_sentiment_twentyfourth_verification_sep04_12am.py",
    "test_type_a_507_verge_openai_ad_monetization_register_boundary_sep04_1am.py",
    "test_type_b_508_kurt_wagner_meta_x_symmetric_accountability_sep04_2am.py",
    "test_type_c_509_anthropic_adweek_zero_deal_posture_sep04_3am.py",
    "test_type_d_510_doc_sync_miss_repair_and_scorer_consistency_sep04_4am.py",
]

# Newest-first expectation, verified against the log 2026-09-04
# (505 D 23:00 through 509 C 03:00, plus this 510 D 04:00 run).
EXPECTED_NEWEST_FIRST = [
    (510, "D"),
    (509, "C"),
    (508, "B"),
    (507, "A"),
    (506, "E"),
]

# Line-anchored heading match only (durable rule from #495b).
_HEADING_RE = re.compile(r"^#(\d+) Type ([A-E]):", re.MULTILINE)


def _is_num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


class TestRotationCycle506to510:
    def test_headings_newest_first_with_expected_types(self):
        text = LOG.read_text()
        positions = {}
        for m in _HEADING_RE.finditer(text):
            num = int(m.group(1))
            if num in (506, 507, 508, 509, 510) and num not in positions:
                positions[num] = (m.start(), m.group(2))
        assert set(positions) == {506, 507, 508, 509, 510}, (
            "missing window headings in iteration-log.md: "
            f"{sorted(set([506,507,508,509,510]) - set(positions))}"
        )
        # Newest-first relative order: 510's heading line precedes 509's, etc.
        offsets = [positions[n][0] for n in (510, 509, 508, 507, 506)]
        assert offsets == sorted(offsets), (
            "window headings are not in newest-first order in iteration-log.md"
        )
        for num, expected_type in EXPECTED_NEWEST_FIRST:
            assert positions[num][1] == expected_type, (
                f"iteration #{num} heading type is {positions[num][1]}, "
                f"expected {expected_type}"
            )


class TestGitOrderConsistency:
    def test_five_type_commits_precede_this_run_in_order(self):
        proc = subprocess.run(
            ["git", "log", "--format=%s", "-10"],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=60,
        )
        nums = []
        for line in proc.stdout.splitlines():
            m = re.search(r"Type [A-E] #(\d+)", line)
            if m:
                nums.append(int(m.group(1)))
            if len(nums) == 5:
                break
        assert nums == [509, 508, 507, 506, 505], (
            f"expected the five pre-run Type commits 509..505 newest-first, "
            f"got {nums}"
        )


class TestWindowDataMechanismIntegrity:
    def test_507_mechanism_key_in_verge_profile(self):
        d = yaml.safe_load((PROFILES / "the-verge.yaml").read_text())
        openai_rel = d["competitor_relationships"]["openai"]
        assert any("mechanism_507" in k for k in openai_rel), (
            "mechanism_507_verge_openai_ad_monetization_register_boundary_condition "
            "missing from the-verge.yaml competitor_relationships.openai"
        )

    def test_509_mechanism_key_in_competitor_entities(self):
        d = yaml.safe_load((PROFILES / "competitor-entities.yaml").read_text())
        anthropic = d["entities"]["anthropic"]
        assert any("509" in str(k) for k in anthropic), (
            "mechanism_509_anthropic_institutionalized_zero_deal_posture "
            "missing from competitor-entities.yaml entities.anthropic"
        )

    def test_508_competitor_coverage_block_on_wagner(self):
        d = yaml.safe_load((PROFILES / "careers" / "journalists.yaml").read_text())
        wagner = [
            j
            for j in d.get("journalists", [])
            if j.get("name") == "Kurt Wagner"
        ]
        assert len(wagner) == 1, "expected exactly one Kurt Wagner journalist entry"
        coverage = wagner[0].get("competitor_coverage", {})
        assert any("508" in str(k) for k in coverage), (
            "type_b_508 competitor_coverage block missing on Kurt Wagner entry"
        )

    def test_506_twentyfourth_cycle_section_in_podcast_log(self):
        text = PODCAST.read_text()
        assert re.search(r"^## Iteration #506 -", text, re.MULTILINE), (
            "no '## Iteration #506' section heading in podcast-sentiment.md"
        )
        assert "wenty-fourth verification cycle" in text, (
            "twenty-fourth verification cycle marker missing from "
            "podcast-sentiment.md"
        )


class TestDocSurfaceCompleteness:
    """Durable fix for the #509 failure mode: a skipped doc-sync must fail
    in the same hour it happens, not one hour later via header totals.

    Two layers: (1) every window test file must have a per-file row in BOTH
    README.md and docs/ARCHITECTURE.md; (2) every window iteration-log entry
    must carry an explicit "Doc sync" section. Layer 2 is the novel catch:
    the #509 entry had no Doc sync section at all - it hand-wrote the
    cumulative file count without performing the sync. #505's
    section-completeness guard checked five other sections; none covers
    the doc-sync step itself."""

    @staticmethod
    def _entry_segment(num):
        text = LOG.read_text()
        headings = [
            (int(m.group(1)), m.start())
            for m in _HEADING_RE.finditer(text)
        ]
        start = next(off for n, off in headings if n == num)
        later = [off for n, off in headings if off > start]
        end = min(later) if later else len(text)
        return text[start:end]

    @pytest.mark.parametrize("fname", WINDOW_FILES)
    def test_row_in_readme(self, fname):
        assert f"`{fname}`" in README.read_text(), (
            f"{fname} has no per-file row in README.md"
        )

    @pytest.mark.parametrize("fname", WINDOW_FILES)
    def test_row_in_architecture(self, fname):
        assert fname in ARCH.read_text(), (
            f"{fname} has no per-file row in docs/ARCHITECTURE.md"
        )

    @pytest.mark.parametrize("fname", WINDOW_FILES)
    def test_readme_row_count_matches_indented_defs(self, fname):
        # Same convention as the structural test_readme_per_file_test_counts:
        # the row claims the indented `def test_` count (raw defs), not the
        # parametrize-expanded collection. Window-scoped, no subprocess.
        content = (TESTS_DIR / fname).read_text()
        actual = len(re.findall(r"^\s+def test_", content, re.MULTILINE))
        m = re.search(
            r"\|\s*`" + re.escape(fname) + r"`\s*\|\s*(\d+)\s*\|",
            README.read_text(),
        )
        assert m, f"no countable README row found for {fname}"
        assert int(m.group(1)) == actual, (
            f"README row for {fname} claims {m.group(1)} tests but the file "
            f"defines {actual} indented test functions"
        )

    @pytest.mark.parametrize("num", [506, 507, 508, 509, 510])
    def test_entry_has_doc_sync_section(self, num):
        segment = self._entry_segment(num)
        assert "Doc sync" in segment, (
            f"iteration #{num} entry has no 'Doc sync' section - the #509 "
            f"failure mode was a performed-in-name-only sync"
        )


class TestScorerEngineConsistencyAudit:
    """Repo-wide audit of every recorded asymmetry_scorer_result block:
    the engine's documented rules must hold for the recorded outputs."""

    @staticmethod
    def _blocks():
        acc = []

        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k == "asymmetry_scorer_result" and isinstance(v, dict):
                        acc.append(v)
                    else:
                        walk(v)
            elif isinstance(o, list):
                for i in o:
                    walk(i)

        for f in PROFILES.rglob("*.yaml"):
            walk(yaml.safe_load(f.read_text()))
        return acc

    def test_significance_flag_follows_p_value_rule(self):
        violations = []
        for b in self._blocks():
            pv, sig = b.get("p_value"), b.get("is_significant")
            if _is_num(pv) and isinstance(sig, bool):
                if sig != (pv < 0.05):
                    violations.append((pv, sig))
        assert not violations, (
            f"is_significant != (p_value < 0.05) in {len(violations)} blocks: "
            f"{violations[:5]}"
        )

    def test_asymmetry_score_equals_target_minus_peer_avg(self):
        violations = []
        for b in self._blocks():
            s = b.get("asymmetry_score")
            t = b.get("target_avg", b.get("target_avg_tone"))
            p = b.get("peer_avg", b.get("peer_avg_tone"))
            if _is_num(s) and _is_num(t) and _is_num(p):
                if abs(s - (t - p)) > 0.051:
                    violations.append((s, t, p))
        assert not violations, (
            f"asymmetry_score != target_avg - peer_avg in {len(violations)} "
            f"blocks: {violations[:5]}"
        )

    def test_recorded_averages_match_tone_lists(self):
        pairs = [
            ("target_avg", "target_tones_manual_illustrative"),
            ("peer_avg", "peer_tones_manual_illustrative"),
            ("target_avg_tone", "target_scores"),
            ("peer_avg_tone", "peer_scores"),
        ]
        violations = []
        for b in self._blocks():
            for avg_key, tones_key in pairs:
                tones, avg = b.get(tones_key), b.get(avg_key)
                if tones and _is_num(avg) and all(_is_num(t) for t in tones):
                    mean = sum(tones) / len(tones)
                    if abs(mean - avg) > 0.051:
                        violations.append((avg_key, mean, avg))
        assert not violations, (
            f"recorded average != mean(tone list) in {len(violations)} blocks: "
            f"{violations[:5]}"
        )

    def test_confidence_intervals_well_ordered(self):
        violations = []
        for b in self._blocks():
            ci = b.get("ci_95", b.get("confidence_interval_95"))
            if (
                isinstance(ci, (list, tuple))
                and len(ci) == 2
                and all(_is_num(c) for c in ci)
            ):
                if not ci[0] < ci[1]:
                    violations.append(tuple(ci))
        assert not violations, (
            f"CI bounds not well-ordered in {len(violations)} blocks: "
            f"{violations[:5]}"
        )

    def test_no_blocks_silently_dropped(self):
        assert len(self._blocks()) >= 28, (
            f"expected at least 28 asymmetry_scorer_result blocks repo-wide, "
            f"found {len(self._blocks())}"
        )
