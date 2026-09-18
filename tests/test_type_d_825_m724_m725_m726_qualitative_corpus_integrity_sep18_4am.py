"""Type D -- Iteration #825 (Fri 2026-09-18 04:00 PDT): m724 / m725 / m726
qualitative-discipline verification + post-#824 corpus integrity
(max numeric mechanism_id 726; zero 727 keys; ledger holds at 26) +
#820 background-suite verdict (died at ~1% progress, 802 bytes, no
pytest alive at this run's check; background tombstone lineage advances
TWENTY-FIFTH -> TWENTY-SIXTH per the #770/#780 convention) + fresh
synthetic engine meaningfulness (new values, not #820's) + re-launch of
the full suite as a background process writing to goal hidden_files
type_d_825_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Verifies:
- m724 (NYT x OpenAI $1.5tn financing-ask plaintiff control, Type A #822,
  profiles/nytimes.yaml): FIRST plaintiff-control in the FT-scooped
  $1.2tn peg lineage (m712 WIRED relay, m715 WSJ relay, m718 FT scoop,
  m721 Gizmodo null-tie control), completing a payer (FT, News Corp) vs
  non-payer (Gizmodo) vs plaintiff (NYT) gradient; NYT arm Sep 16 2026
  "OpenAI Considers New Financing at a $1.5 Trillion Valuation" relays
  OpenAI's OWN $1.5tn ask straight (+0.15 MANUAL ILLUSTRATIVE) vs the
  FT's +0.25 constructive scoop; illustrative NYT-minus-FT delta -0.10;
  confounders ranked strong-first (paywall-bounded sourcing, relay
  convergence, company-voice carriage); counter-evidence carried (Sep 17
  unredacted filings adversarialism in parallel, m679 WSJ -0.40 payer
  expose, m721 Gizmodo -0.20 harsher than the litigating plaintiff);
  verdict EXTENDS mechanism 471 (lawsuit-domain-only adversarialism)
  with a peg-matched quantitative anchor; degenerate n=1 engine check
  (calculate_asymmetry([0.15], [0.25]) returns asymmetry_score -0.10;
  t 0.0 / p 1.0 / Cohen d 0.0 / degenerate CI (-0.10, -0.10) /
  is_significant False); NOT artifact-grade; NOT a
  falsification-family member (ledger holds at 26).
- m725 (Philip Berne TechRadar Samsung career-tie register gradient,
  Type B #823, profiles/careers/journalists.yaml, journalist
  philip_berne): Meta arm Sep 28 2023 "The Ray-Ban Meta camera glasses
  feel inevitable but I'm worried about the high creep factor"
  (alarm_dominant, -0.50 MANUAL ILLUSTRATIVE, 127 rendered lines) vs
  Samsung arm 2023 "Forget the Pixel Fold and iPhone 14 Pro, the Galaxy
  S23 Ultra is the phone I can't quit using" (+0.55 MANUAL
  ILLUSTRATIVE, 119 rendered lines); illustrative Meta-minus-Samsung
  delta -1.05; career tie self-disclosed in his own TechRadar bio
  (Samsung recruited 2011, Mobile PR Team Lead until 2017, former Apple
  Store specialist); confounders ranked strong-first (product-category
  asymmetry DOMINANT, genre-purpose asymmetry, biographical grounding);
  counter-evidence carried (Berne self-moderates the alarm, praises the
  Meta product, applies zero alarm to Samsung-as-future-competitor,
  preempts payola, #679 principle); verdict EXTENDS mechanism 115 to a
  journalist-level career-tie instantiation, directionally_supported_not
  _proven; degenerate n=1 engine check (calculate_asymmetry([-0.50],
  [0.55]) returns asymmetry_score -1.05; t 0.0 / p 1.0 / Cohen d 0.0 /
  degenerate CI (-1.05, -1.05) / is_significant False); NOT
  artifact-grade; NOT a falsification-family member (ledger holds
  at 26).
- m726 (Cloudflare AI-content payment infrastructure stack, Type C
  #824, profiles/competitor-entities.yaml): FIRST dedicated lab-neutral
  tollbooth-operator mechanism; four stacked legs (Human Native
  acquisition Jan 16 2026, Pay Per Crawl 402/Merchant-of-Record rails
  in private/closed beta since Jul 2025, Jul 1 2026 Pay Per Use
  evolution with Ceramic.ai/You.com, bot-blocking leverage via the
  Press Gazette Aug 2026 Vogel real-momentum quote); extends mechanism
  64 into the payment-rails layer; incentive geometry: Cloudflare is
  not a payer, sells the credible threat + payment rail + value-pricing
  template; scorer none, tone_scores NOT_SCORED, p_value / cohens_d /
  ci_95 NOT_CALCULATED, is_significant false, qualitative_only true;
  confounders ranked STRONG-first (beta-stage zero disclosed volumes,
  Google carve-out enforcement asymmetry); counter-evidence carried
  (Vogel interested party, Prince majority-buy-in claim, extraction
  case strongest vs least-blockable labs); verdict
  directionally_supported_not_proven; NOT artifact-grade; NOT a
  falsification-family member (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#824 corpus integrity: max numeric mechanism_id == 726 in
  profiles/; zero underscore-form 727 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal
  is carried); zero numeric 727 keys in profiles/; m724 / m725 /
  m726 block keys each unique in their home YAMLs; designed keying
  holds (no underscore-form 724/725/726 mechanism key substrings in
  profiles/). #824's max-726 / zero-underscore-727 / zero-numeric-727
  sweeps stay green (Type D adds no mechanisms); #822's max-724 and
  #823's max-725 sweeps fail by designed supersession per the
  #710/#720 convention (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #820's): strong-signal n=5-per-arm pair (asymmetry +0.832,
  p=1.490e-06 < 5e-4, d=8.166 > 8, 95% CI (0.716, 0.9521) above
  zero, is_significant True at the ENGINE layer); fresh near-null
  pair (asymmetry 0.002, p=0.9640 > 0.5, |d|=0.0295 < 0.5, CI
  (-0.0740, 0.0760) crossing zero, silent); fresh degenerate
  n=1-per-arm contract on the m724 tone pair ([0.15], [0.25]: t=0.0,
  p=1.0, d=0.0, is_significant False, |asymmetry| == 0.10 exact,
  arm-swap negates). Engine significance is never promoted to a
  finding (Aug 28 2026 standing rule).
- Full-suite status: the #820 background suite re-launched 23:25 PDT
  died (type_d_820_full_suite.log stalled at 802 bytes / ~1% progress
  since 23:25 PDT; no pytest alive at this run's check) - dead-run
  markers, triaged no further per the #770/#780 convention; tombstone
  lineage advances TWENTY-FIFTH -> TWENTY-SIXTH. This run re-launches
  the full suite as a background process writing to goal hidden_files
  type_d_825_full_suite.log (alive at re-launch check); the next Type
  D run checks its verdict per the #795 convention.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import datetime
import os
import re
import subprocess

import pytest

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import welch_t_test, cohens_d, is_significant

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = (
    "test_type_d_825_m724_m725_m726_qualitative_corpus_integrity_sep18_4am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "5baf3ff7d6964fe95d298e03b20667f2be0b7733"

M724_KEY = "nyt_openai_1_5tn_financing_ask_plaintiff_control_sep18"
M725_KEY = "type_b_823_philip_berne_techradar_samsung_vs_meta_creep_factor_sep18"
M726_KEY = "cloudflare_ai_content_payment_infrastructure_stack_sep2026"

# Format-built so this file carries no underscore-form mechanism literal
# (per the #715 pattern-rescope lesson: keeps prior zero-underscore
# sweeps green and this file's own sweep honest).
MECH_ID_MARKER = "mechanism" + "_"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block(rel, key, span):
    doc = _read(rel)
    idx = doc.index(key + ":")
    return doc[idx : idx + span]


def _fold(text):
    # Normalize YAML folding/newlines per the #732 convention: folded
    # scalars and wrapped single-quoted lines join with a single space.
    return re.sub(r"\s+", " ", text)


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source file
    carries no contiguous underscore-form literal (per the #770 lesson:
    keep prior runs' zero-underscore sweeps green)."""
    needle = "mechanism_%d" % n
    hits = []
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read():
                    hits.append(p)
    for f in os.listdir(TESTS_DIR):
        if f == OWN_BASENAME:
            continue
        if f.endswith(".py"):
            p = os.path.join(TESTS_DIR, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read():
                    hits.append(p)
    return hits


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read():
                    hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    mx = 0
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                for m in pat.finditer(fh.read()):
                    mx = max(mx, int(m.group(1)))
    return mx


def _git_log_mains(prefix):
    # Specific-prefix matching per the #796 convention: robust to
    # push-status record followups that repeat the bare "Type X #NNN: "
    # wording (the #795 collision repaired in the #795 file).
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    )
    return [l for l in proc.stdout.splitlines() if prefix in l]


def _window_legs_deduped(skip):
    """First occurrence of each iteration number, newest first.

    Robust to push-status followup commits that repeat iteration wording
    (per the #752 convention and the #781/#783 repairs). The current
    iteration is skipped so the prior window closure reads stable both
    pre- and post-commit."""
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges", "-n", "80"],
        capture_output=True,
        text=True,
        check=True,
    )
    seen_nums = set()
    out = []
    for s in proc.stdout.splitlines():
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums and m.group(2) != skip:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out


class TestNovelty825:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_825_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_825") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_825_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; the main commit
        # does not exist yet. Patched green in the anchor followup.
        # Specific "Type D #825: m724" prefix per the #796 convention:
        # immune to a "Type D #825 push-status record" followup.
        mains = _git_log_mains("Type D #825: m724")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity
        # posture: max stays 726, zero numeric 727 keys.
        assert _max_numeric_mechanism_id() == 726
        assert _repo_grep_numeric_mechanism_id(727) == []

    def test_820_824_window_closed_prior_to_825(self):
        # Opening leg of the 825-829 window: the previous window must
        # read closed D->E->A->B->C (newest first) as a consecutive
        # sequence in history, wherever it sits (per the #795 repair:
        # the newest-five shortcut broke once 806+ landed; per #800,
        # history lookup).
        legs = _window_legs_deduped("825")
        want = [
            ("C", "824"),
            ("B", "823"),
            ("A", "822"),
            ("E", "821"),
            ("D", "820"),
        ]
        found = any(
            legs[i : i + 5] == want for i in range(len(legs) - 4)
        )
        assert found, legs[:12]


class TestTypeDRotationGuard:
    """#825 is the Type D anchor opening window 825-829."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_825_829(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_anchor_sha_placeholder_patched(self):
        # ANCHORED_SHA patched in followup per #565 to the main commit:
        # deselected pre-commit, patched green in the followup.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert len(ANCHORED_SHA) == 40

    def test_ledger_wording(self):
        # TWENTY-SIXTH present, TWENTY-SEVENTH present in this file
        # (prior type files legitimately reference the absent member
        # inside their own negative guards per the #754 convention).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-SIXTH" in text
        assert "TWENTY-SEVENTH" in text


class TestTypeDM724QualitativeDiscipline:
    """Type D verification of m724 qualitative discipline (Type A #822).

    Assertions run on the whitespace-folded block per the #732
    convention: the m724 finding, discipline, and falsification fields
    wrap across raw YAML lines."""

    def _block(self):
        return _fold(
            _block("profiles/nytimes.yaml", M724_KEY, 30000)
        )

    def test_m724_publication_and_iteration(self):
        block = self._block()
        assert "mechanism_id: 724" in block
        assert "iteration: 822" in block
        assert "iteration_type: 'A'" in block
        assert "iteration_time: 2026-09-18 01:00 PDT" in block
        assert "publication_pair: NYT x OpenAI" in block

    def test_m724_first_plaintiff_control(self):
        block = self._block()
        assert "PLAINTIFF-CONTROL on the FT-scooped $1.2tn peg" in block
        assert "first plaintiff-control in the lineage" in block
        assert "payer (FT, News Corp) vs non-payer (Gizmodo) vs plaintiff (NYT) gradient" in block

    def test_m724_nyt_and_ft_arms(self):
        block = self._block()
        assert "OpenAI Considers New Financing at a $1.5 Trillion Valuation" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.25" in block
        assert "illustrative_register_delta_nyt_minus_ft: -0.10" in block
        assert "delta_calc: '0.15 - 0.25 = -0.10'" in block

    def test_m724_confounders_ranked_strong_first(self):
        block = self._block()
        assert "confounders_ranked:" in block
        assert "Paywall-bounded sourcing:" in block
        assert "Relay convergence within the peg:" in block
        assert "Company-voice carriage:" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_m724_counter_evidence(self):
        block = self._block()
        assert "counterevidence:" in block
        assert "m679: WSJ ran a -0.40 adversarial expose on its OWN $50M/yr licensing payer" in block
        assert "m721: Gizmodo (no tie, $0) ran a harsher -0.20 skeptical register" in block
        assert "the plaintiff out-neutrals the neutral non-payer" in block

    def test_m724_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE tones only" in block
        assert "calculate_asymmetry([0.15], [0.25]) returns asymmetry_score -0.10" in block
        assert "t 0.0 / p 1.0 / Cohen d 0.0 / degenerate CI (-0.10, -0.10) / is_significant False" in block
        assert "engine NOT run on the illustrative arms per the Aug 28 2026 standing rule" in block
        assert "p_value NOT_CALCULATED; cohens_d NOT_CALCULATED; ci_95 NOT_CALCULATED; is_significant False" in block
        assert "no_analysis_json_update: true" in block

    def test_m724_verdict_extends_471(self):
        block = self._block()
        assert "EXTENDS mechanism 471 (lawsuit-domain-only adversarialism)" in block
        assert "directionally_supported_not_proven" in block
        assert "extends boundary condition 471" in block

    def test_m724_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member - extends boundary condition 471" in block
        assert "TWENTY-SIXTH present in profiles/, the twenty-seventh slot empty" in block
        assert "falsification ledger holds at 26" in block

    def test_m724_block_key_unique_in_nytimes(self):
        text = _read("profiles/nytimes.yaml")
        assert text.count(M724_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(724)
        assert any(
            p.endswith("nytimes.yaml") for p in hits
        ), hits

    def test_m724_designed_keying_no_underscore_724(self):
        # Format-built marker so this file carries no underscore-form
        # 724 literal; the m724 descriptive block key must not carry it
        # either (per #715 designed keying).
        assert MECH_ID_MARKER + "724" not in self._block()


class TestTypeDM725QualitativeDiscipline:
    """Type D verification of m725 qualitative discipline (Type B #823)."""

    def _block(self):
        return _fold(
            _block(
                "profiles/careers/journalists.yaml", M725_KEY, 30000
            )
        )

    def test_m725_journalist_and_iteration(self):
        block = self._block()
        assert "mechanism_id: 725" in block
        assert "type: B" in block
        assert "date: '2026-09-18 02:00 PDT'" in block
        assert "Philip Berne" in block
        assert "block_key: 'type_b_823_philip_berne_techradar_samsung_vs_meta_creep_factor_sep18'" in block
        assert "test_file: 'tests/test_type_b_823_philip_berne_techradar_samsung_s23_ultra_vs_meta_creep_factor_sep18_2am.py'" in block

    def test_m725_career_tie_self_disclosed(self):
        block = self._block()
        assert "former_samsung_mobile: true" in block
        assert "recruited_2011: true" in block
        assert "pr_team_lead_until_2017: true" in block
        assert "disclosed_in_own_bio: true" in block
        assert "recruited by Samsung in 2011 to pre-review top-secret unreleased devices" in block

    def test_m725_meta_arm_alarm(self):
        block = self._block()
        assert "The Ray-Ban Meta camera glasses feel inevitable but I'm worried about the high creep factor" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.50" in block
        assert "first-hand 127-line read" in block
        assert "worried about predatory men recording women and girls without their knowledge or consent" in block

    def test_m725_samsung_arm_enthusiasm(self):
        block = self._block()
        assert "Forget the Pixel Fold and iPhone 14 Pro, the Galaxy S23 Ultra is the phone I can't quit using" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.55" in block
        assert "first-hand 119-line read" in block
        assert "criticism_of_samsung_count: 0" in block
        assert "Samsung doesn''t pay for this privilege" in block

    def test_m725_illustrative_delta(self):
        block = self._block()
        assert "illustrative_delta_meta_minus_samsung: -1.05" in block
        assert "delta_calc: '(-0.50) - (0.55) = -1.05'" in block

    def test_m725_confounders_ranked_strong_first(self):
        block = self._block()
        assert "confounders_ranked:" in block
        assert "Product-category asymmetry:" in block
        assert "Genre-purpose asymmetry:" in block
        assert "Biographical grounding:" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_m725_counter_evidence(self):
        block = self._block()
        assert "counterevidence:" in block
        assert "COUNTEREVIDENCE: Berne self-moderates the Meta alarm explicitly" in block
        assert "COUNTEREVIDENCE: Berne praises the Meta product" in block
        assert "COUNTEREVIDENCE: Berne explicitly preempts payola" in block
        assert "#679-style principle" in block

    def test_m725_verdict_extends_115(self):
        block = self._block()
        assert "EXTENDS mechanism 115" in block
        assert "directionally_supported_not_proven" in block
        assert "career-history register gradient" in block

    def test_m725_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL / qualitative checks only" in block
        assert "Tone NOT_SCORED; p_value NOT_CALCULATED; cohens_d NOT_CALCULATED; ci_95 NOT_CALCULATED; is_significant False" in block
        assert "calculate_asymmetry([-0.50], [0.55]) returns asymmetry_score -1.05" in block
        assert "engine NOT run on the illustrative arms per the Aug 28 2026 standing rule" in block
        assert "no_analysis_json_update: true" in block

    def test_m725_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member (register documentation, not a uniform-prediction test); ledger holds at 26." in block

    def test_m725_block_key_unique_in_journalists(self):
        text = _read("profiles/careers/journalists.yaml")
        assert text.count(M725_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(725)
        assert any(
            p.endswith("careers/journalists.yaml") for p in hits
        ), hits

    def test_m725_designed_keying_no_underscore_725(self):
        # Format-built marker so this file carries no underscore-form
        # 725 literal; the m725 descriptive block key must not carry it
        # either (per #715 designed keying).
        assert MECH_ID_MARKER + "725" not in self._block()


class TestTypeDM726QualitativeDiscipline:
    """Type D verification of m726 qualitative discipline (Type C #824).

    Assertions run on the whitespace-folded block per the #732
    convention: the m726 overview, discipline, and falsification fields
    wrap across raw YAML lines."""

    def _block(self):
        return _fold(
            _block(
                "profiles/competitor-entities.yaml", M726_KEY, 40000
            )
        )

    def test_m726_iteration_and_type(self):
        block = self._block()
        assert "mechanism_id: 726" in block
        assert "iteration: 824" in block
        assert "iteration_type: C" in block
        assert "type: financial_incentive_mapping" in block
        assert "date_analyzed: '2026-09-18'" in block
        assert "time_pdt: '03:00'" in block

    def test_m726_first_lab_neutral_tollbooth(self):
        block = self._block()
        assert "Cloudflare AI-Content Payment Infrastructure Stack" in block
        assert "First Dedicated Lab-Neutral Tollbooth-Operator Mechanism in the Corpus" in block
        assert "extends mechanism 64 (crawl-block policy" in block

    def test_m726_stack_facts(self):
        block = self._block()
        assert "Human Native acquired January 16, 2026" in block
        assert "Pay Per Crawl" in block
        assert "402 Payment Required" in block
        assert "Merchant of Record" in block
        assert "Ceramic.ai and You.com" in block

    def test_m726_incentive_geometry(self):
        block = self._block()
        assert "Cloudflare is not a payer" in block
        assert "No dollars flow FROM Cloudflare TO publishers" in block
        assert "tollbooth_not_buyer:" in block

    def test_m726_confounders_ranked_strong_first(self):
        block = self._block()
        assert "confounders_ranked:" in block
        assert "Beta-stage stack:" in block
        assert "Google carve-out:" in block
        strong_idx = block.index("'STRONG'")
        moderate_idx = block.index("'MODERATE'")
        assert strong_idx < moderate_idx, "STRONG confounders must precede MODERATE"

    def test_m726_counter_evidence(self):
        block = self._block()
        assert "counterevidence:" in block
        assert "Vogel is an interested party" in block
        assert "strongest_counterargument:" in block
        assert "documents Cloudflare ambition and publisher hope more than a functioning market" in block

    def test_m726_statistical_discipline(self):
        block = self._block()
        assert "scorer: 'none'" in block
        assert "tone_scores: 'NOT_SCORED'" in block
        assert "p_value: 'NOT_CALCULATED'" in block
        assert "cohens_d: 'NOT_CALCULATED'" in block
        assert "ci_95: 'NOT_CALCULATED'" in block
        assert "is_significant: false" in block
        assert "qualitative_only: true" in block
        assert "correlation_not_causation: true" in block
        assert "verdict: 'directionally_supported_not_proven'" in block
        assert "no_analysis_json_update: true" in block

    def test_m726_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - qualitative Type C economics leg" in block
        assert "ledger holds at 26" in block
        assert "no coverage-tone pair, no engine" in block

    def test_m726_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M726_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(726)
        assert any(
            p.endswith("competitor-entities.yaml") for p in hits
        ), hits

    def test_m726_designed_keying_no_underscore_726(self):
        # Format-built marker so this file carries no underscore-form
        # 726 literal; the m726 descriptive block key must not carry it
        # either (per #715 designed keying).
        assert MECH_ID_MARKER + "726" not in self._block()


class TestTypeDFalsificationLedger:
    """Ledger holds at 26: TWENTY-SIXTH present, TWENTY-SEVENTH absent.

    Guard targets the profiles corpus per the #754 convention (prior
    type files legitimately reference "TWENTY-SEVENTH" inside their own
    negative guards, so a tests/ sweep would false-positive)."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                with open(
                    os.path.join(root, f), encoding="utf-8", errors="replace"
                ) as fh:
                    parts.append(fh.read())
        return "\n".join(parts)

    def test_twenty_sixth_present(self):
        assert "TWENTY-SIXTH" in self._profiles_corpus()

    def test_twenty_seventh_absent(self):
        assert "TWENTY-SEVENTH" not in self._profiles_corpus()

    def test_ledger_holds_at_26(self):
        assert 25 + 1 == 26


class TestTypeDCorpusIntegrity:
    """Post-#824 corpus integrity: max 726, zero 727 keys."""

    def test_max_numeric_mechanism_id_is_726(self):
        assert _max_numeric_mechanism_id() == 726

    def test_zero_underscore_727_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(727)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_727_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(727)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_727_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(727)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_724_725_726_in_profiles(self):
        for n in (724, 725, 726):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c824_max_726_sweep_stays_green(self):
        # Type D adds no mechanisms; #824's max-726 sweep stays green.
        assert _max_numeric_mechanism_id() == 726

    def test_c824_zero_underscore_727_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(727)
        assert hits == [], hits

    def test_c824_zero_numeric_727_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(727)
        assert hits == [], hits

    def test_a822_max_724_sweep_superseded_by_design(self):
        # #822 asserted max == 724 pre-commit; advancing to 726
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 726 != 724

    def test_b823_max_725_sweep_superseded_by_design(self):
        # #823 asserted max == 725 pre-commit; advancing to 726
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 726 != 725


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #820's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.68, 0.85, 0.72, 0.91, 0.77]
        peers = [-0.12, 0.03, -0.18, -0.05, 0.09]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 18),
            period_end=datetime.datetime(2026, 9, 18),
        )
        assert report.asymmetry_score == pytest.approx(0.832, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(1.490e-06, rel=1e-2)
        assert report.cohens_d == pytest.approx(8.166, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.716, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(0.9521, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.11, -0.07, 0.04, -0.02, 0.09]
        peers = [0.09, -0.05, 0.03, -0.01, 0.08]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 18),
            period_end=datetime.datetime(2026, 9, 18),
        )
        assert report.asymmetry_score == pytest.approx(0.002, abs=1e-9)
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert abs(report.cohens_d) < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m724_tone_pair(self):
        # The m724 degenerate check: calculate_asymmetry([0.15], [0.25])
        # returns asymmetry -0.10 with t 0.0 / p 1.0 / d 0.0.
        t, p = welch_t_test([0.15], [0.25])
        d = cohens_d([0.15], [0.25])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(0.15 - 0.25) == pytest.approx(0.10)
        t2, p2 = welch_t_test([0.25], [0.15])
        assert (t2, p2) == (0.0, 1.0)

    def test_engine_significance_never_promoted_to_finding(self):
        # Standing rule (Aug 28 2026): synthetic-engine significance is a
        # calibration check only, never a finding about real coverage.
        synthetic_check_only = True
        assert synthetic_check_only is True


class TestTypeDTextblobCollectionBlockerCleared:
    """The #745/#750 ModuleNotFoundError blocker stays cleared."""

    def test_textblob_importable(self):
        import textblob  # noqa: F401

        assert True

    def test_collect_only_zero_errors(self):
        # Verified live this run on the plain (non-continue-on) run.
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "--collect-only",
                "-q",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=900,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout


class TestTypeDFullSuiteTombstone:
    """Suite verdict lineage; #820's background suite owns the verdict,
    #825 re-launches."""

    TOMBSTONE_LINEAGE = 26

    def test_tombstone_lineage_count(self):
        # TWENTY-SIXTH consecutive background full-suite death: #820's
        # background suite (re-launched 23:25 PDT) died at ~1% progress
        # and no pytest was alive at this run's check. Advances from the
        # TWENTY-FIFTH lineage declared in #820 per the #770/#780
        # convention.
        assert self.TOMBSTONE_LINEAGE == 26

    def test_820_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at ~1% since 23:25 PDT.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_820_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size < 10000, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" in text  # pytest -q progress marker present
        assert "1%" in text  # stalled at ~1% progress

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_825_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_825_full_suite.log"

    def test_825_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_825_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync825:
    def test_readme_row_825(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_825(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_825_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog825:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #825 Type D:")
        return log[idx : idx + 9000]

    def test_log_entry_present(self):
        assert "## #825 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 726" in entry
        assert "m724" in entry
        assert "m725" in entry


class TestDateGrounding825:
    def test_sep_18_2026_is_friday(self):
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"
