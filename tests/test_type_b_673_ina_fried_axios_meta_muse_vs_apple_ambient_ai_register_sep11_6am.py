"""Type B #673: Ina Fried (Axios) Meta Muse executive-access business register vs
Apple ambient-AI privacy-virtue headline register, about 48 hours apart.

FIRST dedicated Type B mechanism on Ina Fried (mechanism_id 638, next free
pre-commit; max numeric mechanism_id was 637). Fried is Axios's chief
technology correspondent (~30 years on the tech beat, Axios AI+ newsletter,
"What They Know About You" consumer-AI-privacy series). No Ina Fried
journalist entry existed pre-commit (grep verified: only mention-notes
inside other entries); this run creates it.

Matched pair, same journalist, same publication, Sep 8 -> circa Sep 10,
2026:

(a) Meta arm: Axios Sep 8 2026 "Meta debuts Muse, its long-planned personal
AI agent" (byline Ina Fried per the flipboard Axios author listing attested
this run). Register = executive-access business launch: direct Alexandr
Wang interview ("Wang told Axios"), manifesto tie-in, "long-planned"
coronation framing; privacy covered as product substance (dedicated VM,
privacy architecture, Sentinel human review, no advertising within Muse).
Body text recovered via two verbatim Axios reprints read first-hand
(Slashdot full text, Benton excerpt); axios.com direct fetch
policy-blocked. Tone +0.10 hand-assigned this run (MANUAL ILLUSTRATIVE).

(b) Apple arm: Axios circa Sep 10 2026 "Apple bets on 'ambient AI' without
the always-recording baggage" (byline Ina Fried per her Muck Rack author
page, read first-hand this run). The piece covers Apple Watch and iPhone
ambient-AI features from the Sep 9 event; the dek's "Why it matters" is
explicit privacy virtue: "Apple is aiming to show it can be more private
and useful, even as it plays catch-up to the state of the art in AI."
Register = privacy-virtue headline. Tone +0.30 hand-assigned this run
(MANUAL ILLUSTRATIVE), scored on headline/dek only. Evidence tier:
headline-and-dek bounded (body not recovered; axios.com policy-blocked).

Finding: gradient-absent headline-register contrast with strong news-peg
confounds. The same Axios journalist who frames Meta's agent launch
through an executive-access business register gives Apple's ambient-AI
wearables features a privacy-virtue headline about 48 hours later, even
though Meta's own launch carried substantive privacy architecture that the
headline did not virtue-signal. No one-sided financial gradient predicts a
Meta-vs-Apple gap at Axios (the corpus holds no verified AI-lab
licensing/payment leg for Axios), so this pair is a gradient-absent case in
the #663 family, NOT a falsification-family member and NOT a pure
asymmetry pin. The STRONG news-peg confound (standalone launch with a
granted executive interview vs hardware-event feature coverage) is the
leading alternative explanation: register follows access.

Honest bound (same journalist, entity-neutral launch register): Fried's
Axios piece "Welcome to the AGI era," OpenAI says as GPT-6 Astra debuts
gives OpenAI the same executive-access coronation register as the Meta arm
("generational leap", Brockman interview). The launch register is
entity-neutral; the Meta-vs-Apple gap is headline-level and story-type
driven, not entity-animus driven. Further counterevidence: Fried's Aug 20
2026 "OpenAI to rewrite its safety rules post-Hugging Face" runs
accountability register on OpenAI.

Illustrative delta (Apple minus Meta) = 0.30 - 0.10 = +0.20 (IEEE-inexact
0.19999999999999998; 1e-9 tolerance per the #668 convention);
p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28
standing rule); statistical_contract degenerate_n1_per_arm. No engine run.

Novelty vs prior work: FIRST dedicated Type B on Ina Fried; no journalist
entry pre-commit; both arms new to a same-journalist mechanism; the Apple
ambient-AI piece is new-to-corpus (zero repo-wide hits for
"always-recording" pre-commit, grep verified). Overrides the prior
not-pursued research notes (journalists.yaml lines 15957 and 18100:
Bobrowsky-entry note and Silberling-entry research_method, both recording
"Ina Fried/Axios policy-blocked, no resolvable first-party URLs, not
pursued") with new evidence: flipboard byline attestation, verbatim reprint
bodies, first-hand Muck Rack author-page read. Distinct from #668 (Newman,
WIRED, different register pair); extends the cross-entity
wearable-register comparison to a second journalist/publication per the
#648 Dave precedent for a new angle.

Rotation: Type B follows Type A (#672) per A,B,C,D,E. Rotation guard and
doc-sync deselected pre-commit per the #565 followup convention; anchor
patched in the followup commit once the main commit SHA is known.
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

MECH_KEY = "mechanism_638_ina_fried_axios_meta_muse_vs_apple_ambient_ai_register_sep08_sep10"
FILENAME = "test_type_b_673_ina_fried_axios_meta_muse_vs_apple_ambient_ai_register_sep11_6am.py"

META_TONE = 0.10
APPLE_TONE = 0.30
EXPECTED_DELTA = 0.20

META_URLS = [
    "https://meta.slashdot.org/story/26/09/08/2012246/meta-debuts-muse-its-long-planned-personal-ai-agent",
    "https://www.benton.org/headlines/meta-debuts-muse-its-long-planned-personal-ai-agent",
    "https://flipboard.com/@axiosnews/stories-by-ina-fried-c0n8an9kz",
]
APPLE_URLS = [
    "https://muckrack.com/inafried/articles",
]

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "0bfea2a"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


def _fried():
    matches = []
    for j in _careers()["journalists"]:
        if isinstance(j, dict) and j.get("name") == "Ina Fried":
            matches.append(j)
    assert len(matches) == 1, f"expected exactly one Ina Fried entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    fried = _fried()
    assert MECH_KEY in fried, f"{MECH_KEY} missing from Ina Fried entry"
    return fried[MECH_KEY]


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


class TestIterationMetadata673:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 673

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 638

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 638:
                    seen.setdefault(638, []).append(path)
        assert len(seen.get(638, [])) == 1, f"mechanism_id 638 not unique: {seen.get(638)}"

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_673_ina_fried_axios_meta_muse_vs_apple_ambient_ai_register_sep08_sep10"

    def test_first_dedicated_type_b_on_fried(self):
        fried = _fried()
        dedicated = [k for k in fried
                     if k.startswith("mechanism_") and "crossref" not in k and "cross_ref" not in k]
        assert MECH_KEY in dedicated, f"mechanism 638 missing from dedicated list: {dedicated}"
        assert not any("ina_fried" in k and k != MECH_KEY for k in dedicated), (
            f"unexpected second Fried dedicated mechanism: {dedicated}"
        )

    def test_no_duplicate_673_file(self):
        others = [p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_673_*.py"))
                  if os.path.basename(p) != FILENAME]
        assert not others, f"duplicate #673 test files: {others}"


class TestFriedArms673:
    def test_meta_arm_date_and_byline(self):
        meta = _mechanism()["meta_arm"]
        assert meta["date"] == "2026-09-08"
        assert "Ina Fried" in meta["piece"]
        assert "Axios" in meta["piece"]

    def test_meta_arm_url_verbatim(self):
        urls = _mechanism()["meta_arm"]["source_urls"]
        for u in META_URLS:
            assert u in urls, f"meta URL missing: {u}"

    def test_meta_arm_wang_interview_quote(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("Wang told Axios" in q for q in quotes)

    def test_meta_arm_privacy_substance_quotes(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("no advertising within Muse" in q for q in quotes)
        assert any("dedicated virtual machine" in q for q in quotes)
        assert any("Sentinel" in q for q in quotes)

    def test_meta_arm_rayban_glasses_callback(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("Ray-Ban smart glasses" in q for q in quotes)

    def test_meta_arm_register_is_executive_access(self):
        assert _mechanism()["meta_arm"]["register"] == "executive_access_business_launch"

    def test_meta_arm_source_note_names_block(self):
        note = _mechanism()["meta_arm"]["source_note"]
        assert "policy-blocked" in note
        assert "axios.com" in note
        assert "verbatim" in note

    def test_apple_arm_date_and_byline(self):
        apple = _mechanism()["apple_arm"]
        assert apple["date"] == "2026-09-10"
        assert "Ina Fried" in apple["piece"]
        assert "Axios" in apple["piece"]

    def test_apple_arm_url_verbatim(self):
        urls = _mechanism()["apple_arm"]["source_urls"]
        for u in APPLE_URLS:
            assert u in urls, f"apple URL missing: {u}"

    def test_apple_arm_privacy_virtue_headline(self):
        quotes = _mechanism()["apple_arm"]["evidence_quotes"]
        assert any("always-recording baggage" in q for q in quotes)

    def test_apple_arm_dek_privacy_virtue(self):
        quotes = _mechanism()["apple_arm"]["evidence_quotes"]
        assert any("more private and useful" in q for q in quotes)

    def test_apple_arm_headline_bounded_note(self):
        note = _mechanism()["apple_arm"]["source_note"]
        assert "Headline-and-dek bounded" in note

    def test_apple_arm_register_is_privacy_virtue(self):
        assert _mechanism()["apple_arm"]["register"] == "privacy_virtue_headline"

    def test_same_journalist_both_arms_about_48h_apart(self):
        meta = _mechanism()["meta_arm"]
        apple = _mechanism()["apple_arm"]
        assert "Ina Fried" in meta["byline"]
        assert "Ina Fried" in apple["byline"]
        assert meta["date"] == "2026-09-08"
        assert apple["date"] == "2026-09-10"

    def test_bound_arm_openai_entity_neutral(self):
        bound = _mechanism()["bound_arm_openai"]
        assert "generational leap" in bound["note"]
        assert "entity-neutral" in bound["note"]
        assert "Title-and-dek bounded" in bound["source_note"]


class TestScorerDelta673:
    def test_delta_math(self):
        s = _mechanism()["asymmetry_scorer"]
        assert s["meta_tone"] == META_TONE
        assert s["apple_tone"] == APPLE_TONE
        # 0.30 - 0.10 is IEEE-inexact (0.19999999999999998); tolerance per
        # the #668 convention, documented as float-representation nuance.
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
        assert "Hypothesis-generating only" in verdict

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
        assert any("headline-and-dek only" in s for s in c["strong"])
        assert any("Access asymmetry" in s for s in c["moderate"])
        assert any("inference, recorded as such" in s for s in c["moderate"])
        assert any("n=1 per arm" in s for s in c["weak"])

    def test_counterevidence_present(self):
        ce = _mechanism()["counterevidence"]
        joined = " ".join(ce)
        assert "generational leap" in joined
        assert "entity-neutral" in joined
        assert "rewrite its safety rules" in joined
        assert "headline-register, not body-omission" in joined

    def test_cross_refs_name_prior_work(self):
        refs = _mechanism()["cross_references"]
        joined = " ".join(refs)
        assert "#668" in joined
        assert "#663" in joined
        assert "#653" in joined
        assert "mechanism 635" in joined
        assert "not-pursued" in joined


class TestFinancialContext673:
    def test_no_verified_axios_gradient(self):
        fc = _mechanism()["financial_context"]
        assert "no verified AI-lab licensing or payment leg for Axios" in fc

    def test_correlation_not_causation(self):
        fc = _mechanism()["financial_context"]
        assert "Correlation, not causation" in fc

    def test_news_peg_leads_money(self):
        fc = _mechanism()["financial_context"]
        assert "stronger than any money story" in fc


class TestRotationCycleGuard673:
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

    def test_window_669_673_closes_c_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "673"),
            ("A", "672"),
            ("E", "671"),
            ("D", "670"),
            ("C", "669"),
        ], f"rotation window 669-673 wrong: {observed}"

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
        # Post-commit anchor: the #673 main commit. Patched in the followup
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
        assert subject.startswith("Type B #673:"), (
            f"post-commit anchor broken: newest main is not #673: {subject!r}"
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
        sample = "Type B #673: Ina Fried Axios Meta Muse vs Apple ambient-AI register"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "673", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet673:
    def test_readme_has_673_row(self):
        assert "#673" in read_readme()

    def test_arch_has_673_row(self):
        assert "673" in read_arch()

    def test_readme_row_mentions_fried(self):
        assert "Fried" in read_readme()

    def test_log_starts_with_673(self):
        assert read_log_start().startswith("#673 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #673 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #673 row should mention this file's def-test count {n}"
        )


class TestNoBrittlePatterns673:
    def test_yaml_reparses_clean(self):
        fried = _fried()
        m = fried[MECH_KEY]
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
