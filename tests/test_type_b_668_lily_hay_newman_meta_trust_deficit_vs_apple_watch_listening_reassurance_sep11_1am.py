"""Type B #668: Lily Hay Newman (WIRED) Meta Muse trust-deficit vs Apple Watch
listening-reassurance register asymmetry, 23 hours apart.

FIRST dedicated Type B mechanism on Lily Hay Newman (mechanism_id 635, next
free pre-commit; max numeric mechanism_id was 634). Newman is WIRED's senior
security/privacy writer (~9-year tenure, 2017-present) with zero prior
dedicated Type B mechanisms (journalists.yaml entry verified mechanism-free
this run).

Matched pair, same journalist, same security/ambient-data beat, 23 hours
apart (Sep 8 -> Sep 9, 2026):

(a) Meta arm: WIRED Sep 8 2026 "Meta Releases Muse, a Personal AI Agent With
Privacy 'Built Into It'" (byline Lily Hay Newman + Maxwell Zeff per the
verbatim reprint mirror; WIRED also ran the headline variant "Muse, Meta's
New Personal AI Agent, Needs You To Trust It" per the Muck Rack listing and
the #647 corpus entry). Register = launch framed through a trust deficit:
the trust-skeptical headline variant makes Meta's credibility the lede
obstacle for its biggest consumer AI launch. Tone -0.30 hand-assigned this
run (MANUAL ILLUSTRATIVE), matching the #647 pin on this exact article for
corpus consistency.

(b) Apple arm: WIRED Sep 9 2026 "Apple Doesn't Want You to Worry About the
New Apple Watch's Listening Features" (byline Lily Hay Newman solo per the
verbatim reprint mirror). The piece covers Apple Watch Series 12 / Ultra 4
"audio intelligence": four opt-in tools powered by audio gathered by the
watch microphones, including Live Rewind surfacing the last 15 seconds of
ambient conversation as text (wired.jp edition snippet). Register =
reassurance-adoption: the headline adopts Apple's own worry-dismissal frame
verbatim, even as Apple itself is wary users may feel constantly listened
to. The dek carries a real skeptical caveat ("But the protections can't
change the facts of what the tools do"), so the register gap is
headline-level, not full-article inversion - the mechanism records this as a
mixed register, honestly bounded. Tone +0.10 hand-assigned this run (MANUAL
ILLUSTRATIVE): net mildly reassuring.

Finding: gradient-absent register asymmetry with strong news-peg
confounds. The same security-desk journalist who frames Meta's agent launch
through a trust deficit adopts Apple's reassurance frame as a headline 23
hours later for always-on microphone hardware. No one-sided financial
gradient predicts a Meta-vs-Apple gap at WIRED (Condé Nast receives
$5-10M/yr from OpenAI licensing; Apple is not a Condé Nast AI-licensing
deal partner per the corpus), so this pair is a gradient-absent case in the
#663 family, NOT a falsification-family member and NOT a pure asymmetry
pin. The STRONG news-peg confound (a data-hungry agent launch two weeks
after the $18B settlement vs opt-in watch features) is the leading
alternative explanation.

Honest bound (same journalist, deal-partner adversarial): Newman's WIRED
piece "OpenAI's Hugging Face Hack Debrief Raises More Questions Than It
Answers" runs adversarial on OpenAI, the $5-10M/yr deal partner. WIRED's
security desk does not go easy on deal partners; the register gap here is
better explained by news-peg and beat norms than by money.

Illustrative delta (Apple minus Meta) = 0.10 - (-0.30) = +0.40;
p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28
standing rule); statistical_contract degenerate_n1_per_arm. No engine run
(the next Type D battery-verifies the degenerate contract per the #663/#665
convention).

Novelty vs prior work: FIRST dedicated Type B on Lily Hay Newman; both
WIRED headline variants of the Meta arm are new to a same-journalist
mechanism (the #647 Type A used this Meta article at publication level,
mechanism 622 - this run adds the same-journalist Apple comparator, a new
angle per the #648 Dave precedent); the Apple Watch listening piece is
new-to-corpus (zero repo-wide hits pre-commit, grep verified). Distinct
from #653 (Hart, different journalist and publication) and #647 (WIRED
publication-level, Anthropic comparator, not Apple).

Rotation: Type B follows Type A (#667) per A,B,C,D,E. Rotation guard
deselected pre-commit per the #565 followup convention; anchor patched in
the followup commit once the main commit SHA is known.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_635_lily_hay_newman_meta_muse_trust_deficit_vs_apple_watch_listening_reassurance_sep08_sep09"
FILENAME = "test_type_b_668_lily_hay_newman_meta_trust_deficit_vs_apple_watch_listening_reassurance_sep11_1am.py"

META_TONE = -0.30
APPLE_TONE = 0.10
EXPECTED_DELTA = 0.40

META_URLS = [
    "https://technewstube.com/wired/1865498/meta-releases-muse-personal-ai-agent-privacy-built-into/",
    "https://muckrack.com/lily-hay-newman/articles",
]
APPLE_URLS = [
    "https://technewstube.com/wired/1865899/apple-doesnt-to-worry-new-apple-watchs-listening/",
]

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "0000000"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


def _newman():
    matches = []
    for j in _careers()["journalists"]:
        if isinstance(j, dict) and j.get("name") == "Lily Hay Newman":
            matches.append(j)
    assert len(matches) == 1, f"expected exactly one Lily Hay Newman entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    newman = _newman()
    assert MECH_KEY in newman, f"{MECH_KEY} missing from Lily Hay Newman entry"
    return newman[MECH_KEY]


def _mechanism_text():
    return yaml.safe_dump(_mechanism(), allow_unicode=True)


def _count_def_tests():
    path = os.path.join(TESTS_DIR, FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestIterationMetadata668:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 668

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 635

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 635:
                    seen.setdefault(635, []).append(path)
        assert len(seen.get(635, [])) == 1, f"mechanism_id 635 not unique: {seen.get(635)}"

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_668_lily_hay_newman_meta_muse_trust_deficit_vs_apple_watch_listening_reassurance_sep08_sep09"

    def test_first_dedicated_type_b_on_newman(self):
        newman = _newman()
        dedicated = [k for k in newman
                     if k.startswith("mechanism_") and "crossref" not in k and "cross_ref" not in k]
        assert MECH_KEY in dedicated, f"mechanism 635 missing from dedicated list: {dedicated}"
        assert not any("lily_hay_newman" in k and k != MECH_KEY for k in dedicated), (
            f"unexpected second Newman dedicated mechanism: {dedicated}"
        )

    def test_no_duplicate_668_file(self):
        others = [p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_668_*.py"))
                  if os.path.basename(p) != FILENAME]
        assert not others, f"duplicate #668 test files: {others}"


class TestNewmanArms668:
    def test_meta_arm_date_and_byline(self):
        meta = _mechanism()["meta_arm"]
        assert meta["date"] == "2026-09-08"
        assert "Lily Hay Newman" in meta["piece"]
        assert "Maxwell Zeff" in meta["piece"]
        assert "WIRED" in meta["piece"]

    def test_meta_arm_url_verbatim(self):
        urls = _mechanism()["meta_arm"]["source_urls"]
        for u in META_URLS:
            assert u in urls, f"meta URL missing: {u}"

    def test_meta_arm_trust_deficit_headline_variant(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("Needs You To Trust It" in q for q in quotes)
        assert any("Privacy" in q and "Built Into It" in q for q in quotes)

    def test_meta_arm_mirror_byline_timestamp(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("Sep 8, 2026, 4:12 pm" in q for q in quotes)

    def test_meta_arm_register_is_trust_deficit(self):
        assert _mechanism()["meta_arm"]["register"] == "launch_framed_through_trust_deficit"

    def test_meta_arm_source_note_names_tiers(self):
        note = _mechanism()["meta_arm"]["source_note"]
        assert "mirror-bounded" in note
        assert "wired.com" in note and "policy-blocked" in note

    def test_apple_arm_date_and_byline(self):
        apple = _mechanism()["apple_arm"]
        assert apple["date"] == "2026-09-09"
        assert "Lily Hay Newman" in apple["piece"]
        assert "WIRED" in apple["piece"]
        assert "Zeff" not in apple["piece"]

    def test_apple_arm_url_verbatim(self):
        urls = _mechanism()["apple_arm"]["source_urls"]
        for u in APPLE_URLS:
            assert u in urls, f"apple URL missing: {u}"

    def test_apple_arm_reassurance_headline(self):
        quotes = _mechanism()["apple_arm"]["evidence_quotes"]
        assert any("Doesn" in q and "Worry" in q and "Listening Features" in q for q in quotes)

    def test_apple_arm_mirror_byline_timestamp(self):
        quotes = _mechanism()["apple_arm"]["evidence_quotes"]
        assert any("Sep 9, 2026, 3:14 pm" in q for q in quotes)

    def test_apple_arm_skeptical_dek_caveat_recorded(self):
        quotes = _mechanism()["apple_arm"]["evidence_quotes"]
        assert any("protections can" in q and "change the facts" in q for q in quotes)

    def test_apple_arm_hardware_detail_recorded(self):
        quotes = _mechanism()["apple_arm"]["evidence_quotes"]
        assert any("audio intelligence" in q for q in quotes)
        assert any("Live Rewind" in q for q in quotes)

    def test_apple_arm_register_is_mixed_reassurance(self):
        assert _mechanism()["apple_arm"]["register"] == "reassurance_adoption_with_skeptical_dek_caveat"

    def test_same_journalist_both_arms_23h_apart(self):
        meta = _mechanism()["meta_arm"]
        apple = _mechanism()["apple_arm"]
        assert "Lily Hay Newman" in meta["piece"]
        assert "Lily Hay Newman" in apple["piece"]
        assert meta["date"] == "2026-09-08"
        assert apple["date"] == "2026-09-09"

    def test_bound_arm_openai_adversarial_recorded(self):
        bound = _mechanism()["bound_arm_openai"]
        assert "Hugging Face Hack Debrief" in bound["piece"]
        assert "More Questions Than It Answers" in bound["piece"]
        assert "title-bounded" in bound["source_note"].lower()


class TestScorerDelta668:
    def test_delta_math(self):
        s = _mechanism()["asymmetry_scorer"]
        assert s["meta_tone"] == META_TONE
        assert s["apple_tone"] == APPLE_TONE
        # 0.10 - (-0.30) is IEEE-inexact (0.4000000000000000222); tolerance
        # per the #665 convention, documented as float-representation nuance.
        assert abs(s["illustrative_delta_apple_minus_meta"] - EXPECTED_DELTA) < 1e-9
        assert abs((APPLE_TONE - META_TONE) - EXPECTED_DELTA) < 1e-9

    def test_manual_illustrative_only(self):
        text = _mechanism_text()
        assert "MANUAL" in text
        s = _mechanism()["asymmetry_scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["statistical_contract"] == "degenerate_n1_per_arm"

    def test_verdict_boundaries(self):
        verdict = _mechanism()["asymmetry_scorer"]["verdict"]
        assert "NOT a falsification-family member" in verdict
        assert "NOT a pure asymmetry pin" in verdict
        assert "Correlation only, not causation" in verdict

    def test_verdict_gradient_absent(self):
        verdict = _mechanism()["asymmetry_scorer"]["verdict"]
        assert "Gradient-absent" in verdict
        assert "#663 family" in verdict

    def test_confounder_strengths_ranked(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 2
        assert len(c["moderate"]) == 2
        assert len(c["weak"]) == 2
        assert any("News-peg" in s for s in c["strong"])
        assert any("$18B settlement" in s for s in c["strong"])
        assert any("Co-byline dilution" in s for s in c["strong"])
        assert any("headline-level" in s.lower() for s in c["moderate"])
        assert any("Beat-register" in s for s in c["moderate"])
        assert any("n=1 per arm" in s for s in c["weak"])

    def test_counterevidence_present(self):
        ce = _mechanism()["counterevidence"]
        joined = " ".join(ce)
        assert "hugging face hack debrief" in joined.lower()
        assert "deal partner" in joined
        assert "does not go easy on deal partners" in joined

    def test_cross_refs_name_prior_work(self):
        refs = _mechanism()["cross_references"]
        joined = " ".join(refs)
        assert "#647" in joined
        assert "#599" in joined
        assert "#663" in joined
        assert "#653" in joined
        assert "mechanism 622" in joined


class TestFinancialContext668:
    def test_condenast_openai_licensing_named(self):
        fc = _mechanism()["financial_context"]
        assert "$5-10M/yr" in fc
        assert "OpenAI" in fc

    def test_no_onesided_meta_apple_gradient(self):
        fc = _mechanism()["financial_context"]
        assert "not a Cond" in fc or "no Cond" in fc or "Apple is not" in fc
        assert "no one-sided" in fc.lower()

    def test_correlation_not_causation(self):
        fc = _mechanism()["financial_context"]
        assert "Correlation, not causation" in fc

    def test_news_peg_leads_money(self):
        fc = _mechanism()["financial_context"]
        assert "news-peg" in fc


class TestRotationCycleGuard668:
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

    def test_window_664_668_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "668"),
            ("A", "667"),
            ("E", "666"),
            ("D", "665"),
            ("C", "664"),
        ], f"rotation window 664-668 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #668 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha.startswith(ANCHORED_SHA), f"anchor not yet patched: {sha}"
        assert subject.startswith("Type B #668:"), (
            f"post-commit anchor broken: newest main is not #668: {subject!r}"
        )

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type B #668: Lily Hay Newman Meta trust-deficit vs Apple Watch reassurance"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "668", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet668:
    def test_readme_has_668_row(self):
        assert "#668" in read_readme()

    def test_arch_has_668_row(self):
        assert "668" in read_arch()

    def test_readme_row_mentions_newman(self):
        assert "Newman" in read_readme()

    def test_log_starts_with_668(self):
        assert read_log_start().startswith("#668 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #668 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #668 row should mention this file's def-test count {n}"
        )


class TestNoBrittlePatterns668:
    def test_yaml_reparses_clean(self):
        newman = _newman()
        m = newman[MECH_KEY]
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["meta_arm"]["tone_illustrative"], float)
        assert isinstance(m["apple_arm"]["tone_illustrative"], float)
        assert isinstance(m["asymmetry_scorer"]["is_significant"], bool)

    def test_no_em_dash_in_mechanism(self):
        assert "\u2014" not in _mechanism_text()
        assert "\u2028" not in _mechanism_text()
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        assert "\u2014" not in src
        assert "\u2028" not in src

    def test_all_urls_http_or_https(self):
        urls = list(_mechanism()["meta_arm"]["source_urls"]) + \
            list(_mechanism()["apple_arm"]["source_urls"])
        assert urls, "no URLs recorded"
        for u in urls:
            assert u.startswith(("http://", "https://")), f"bad URL: {u!r}"

    def test_no_zero_coverage_claims(self):
        text = _mechanism_text().lower()
        assert "zero coverage" not in text
        assert "no coverage" not in text

    def test_no_engine_significance_claims(self):
        text = _mechanism_text().lower()
        assert "statistically significant" not in text
        assert "p < 0.05" not in text
        assert "p<0.05" not in text

    def test_research_method_names_evidence_tiers(self):
        rm = _mechanism()["research_method"]
        assert "First-hand" in rm or "first-hand" in rm
        assert "verbatim" in rm

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _mechanism()["artifact_readiness"]
