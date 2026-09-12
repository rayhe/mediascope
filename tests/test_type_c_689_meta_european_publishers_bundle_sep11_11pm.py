"""Type C #689: Meta x European Publishers Bundle (Le Figaro / Prisa /
Suddeutsche Zeitung) March 2026 AI news licensing deal formalization -
the FIRST dedicated deal-level mechanism on Meta's European payer leg.

Meta's own about.fb.com announcement (~Mar 13 2026, French edition):
new partnerships with News Corp, Le Figaro, Prisa, and Suddeutsche
Zeitung, in continuation of previous partnerships with other media
including Le Monde. Meta AI news answers will carry information and
links from these outlets; "just the beginning" of an expanding
publisher network. Financial terms not publicly disclosed (Seeking
Alpha). eloutput (English): initial phase, European users first, spans
breaking news to entertainment/lifestyle. abit.ee (Mar 13 2026, in
Estonian): four languages/political views; publisher calculus (audience
vs training systems that could reduce traffic). Engadget (updated Mar 3
2026): Meta had already signed multi-year agreements with USA Today,
People, CNN, Fox News. WSJ via E&P (Mar 4 2026, Alexandra Bruell): the
News Corp leg alone pays up to $50M a year for at least three years
with retrieval plus archive-training rights. Only the News Corp leg
carries a disclosed quantum; the European legs' terms are confidential
and training rights unconfirmed. Sep 2026 status ACTIVE per the #599
convention (bounded absence of exit reporting per the iteration-492
rule). Falsification pin: El Pais (Prisa's flagship daily) Aug 30
2026, "Los otros vertidos toxicos del imperio Zuckerberg: limpieza
etnica, explotacion masiva de datos y desinformacion" (the other toxic
spills of the Zuckerberg empire: ethnic cleansing, massive data
exploitation and disinformation), anchored on the $18B multistate
youth-harms settlement - hard accountability from a Meta-paid
counterparty; MANUAL ILLUSTRATIVE -0.55 (excerpt-bounded, Spanish
original, not opened first-hand). SEVENTEENTH falsification-family
member (ledger at 16 after #688); second Meta-payer pin (first: #664
mechanism 633, Reuters -0.45 on the Muse launch). Corroborating only:
Le Monde (named by Meta as a previous AI partner) Aug 11 2026, "dix
ans d'hesitations et une volte-face de Zuckerberg" - hard register,
weaker leg-status evidence. Cross-outlet nuance: same payer, divergent
registers - WSJ Bobrowsky +0.40 aspirational (News Corp leg #549, #662),
Reuters Katie Paul -0.45 accountability (Reuters leg #633, #664), El
Pais toxic-spills accountability -0.55 illustrative (Prisa leg, this
run). Payment direction alone does not determine register.
Tone-predictor grade MODERATE-WEAK (AI-chatbot grounding inside Meta's
own product, but quantum undisclosed, training rights unconfirmed,
voluntary non-exclusive, link-out traffic design). No tone scores,
qualitative only, no engine run, NOT artifact-grade. Distinct from
mechanism 549 (News Corp leg, same tranche), mechanism 633 (Reuters
leg), #664 (the run that minted 633), mechanism 642 (Apple News+ WEAK
grade comparator), mechanism 539/443/504/564/391 (prior legs).
Correlation only.

Research method: 3 browser.search query sets, all excerpt-bounded; no
first-hand page opens this run (elpais.com, lemonde.fr, about.fb.com
read via search-result excerpts). All URLs verbatim from Full-URL
listings; no canonical URLs constructed. No zero-coverage claims.

Rotation: Type C follows Type B (#688) per A,B,C,D,E. Rotation guard,
doc-sync, and novelty-anchor tests deselected pre-commit per the #565
followup convention; anchor patched in the followup commit once the
main commit SHA is known.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_648_meta_european_publishers_bundle_mar2026"
FILENAME = "test_type_c_689_meta_european_publishers_bundle_sep11_11pm.py"

ABOUTFB_URL = "https://about.fb.com/fr/news/2026/03/meta-annonce-un-nouveau-partenariat-avec-plusieurs-medias-dont-le-figaro-pour-enrichir-meta-ai-avec-davantage-dactualites-et-de-contenus-internationaux/"
SEEKINGALPHA_URL = "https://seekingalpha.com/news/4564325-meta-strikes-news-content-deal-with-wsj-owner-leading-european-media-firms"
ELOUTPUT_URL = "https://en.eloutput.com/news/social-media/meta-ai-will-integrate-news-from-major-international-media-outlets-in-Europe/"
ABIT_URL = "https://abit.ee/et/tehisintellekt/meta-ai-news-le-figaro-sddeutsche-zeitung-news-corp-prisa-media-partnership-et"
ENGADGET_URL = "https://www.engadget.com/ai/meta-signs-a-multimillion-dollar-ai-licensing-deal-with-news-corp-234157902.html"
EP_URL = "https://www.editorandpublisher.com/stories/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year,260471"
ELPAIS_URL = "https://elpais.com/tecnologia/2026-08-30/los-otros-vertidos-toxicos-del-imperio-zuckerberg-limpieza-etnica-explotacion-masiva-de-datos-y-desinformacion.html"
LEMONDE_URL = "https://www.lemonde.fr/series-d-ete/article/2026/08/11/facebook-et-les-fausses-informations-dix-ans-d-hesitations-et-une-volte-face-de-zuckerberg_6744010_3451060.html"
LLMPULSE_URL = "https://llmpulse.ai/blog/ai-content-licensing-deals/"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "b95def6"


def _entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def _meta():
    return _entities()["entities"]["meta"]


def _mechanism():
    m = _meta()
    assert MECH_KEY in m, f"{MECH_KEY} missing from entities.meta"
    return m[MECH_KEY]


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


class TestIterationMetadata689:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 689

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 648

    def test_mechanism_id_unique_repo_wide(self):
        # Per the #674 convention: only this run's mechanism_id is asserted
        # unique (legacy ids like 80 have pre-existing corpus collisions).
        seen = []
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 648:
                    seen.append(path)
        assert len(seen) == 1, f"mechanism_id 648 not unique: {seen}"
        assert seen[0].endswith("competitor-entities.yaml")

    def test_rotation_type_c(self):
        assert _mechanism()["rotation"] == "Type C"

    def test_job_and_goal_ids(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_type_c_focus_names_first_dedicated(self):
        assert "FIRST dedicated deal-level mechanism" in _mechanism()["type_c_focus"]


class TestDealLegFormalization689:
    def test_announcement_date_march_2026(self):
        assert "2026-03-13" in _mechanism()["announcement_date"]

    def test_four_counterparties(self):
        terms = _mechanism()["deal_terms"]["counterparties"]
        for name in ("Le Figaro", "Prisa", "Suddeutsche Zeitung", "News Corp"):
            assert name in terms, f"counterparty missing: {name}"

    def test_terms_undisclosed_with_quantum_caveat(self):
        value = _mechanism()["deal_terms"]["value"]
        assert "not publicly disclosed" in value
        assert "Seeking Alpha" in value
        assert "$50M/yr" in value or "$50M" in value

    def test_scope_meta_ai_rag_grounding(self):
        scope = _mechanism()["deal_terms"]["scope"]
        assert "Meta AI" in scope
        assert "links to the original articles" in scope

    def test_le_monde_prior_partner_named(self):
        prior = _mechanism()["deal_terms"]["prior_partners"]
        assert "Le Monde" in prior

    def test_training_rights_undisclosed_for_european_legs(self):
        tr = _mechanism()["deal_terms"]["training_rights"]
        assert "UNDISCLOSED" in tr
        assert "News Corp leg" in tr

    def test_prior_us_bundle_context(self):
        prior = _mechanism()["deal_terms"]["prior_partners"]
        for name in ("USA Today", "People", "CNN", "Fox News"):
            assert name in prior, f"prior partner missing: {name}"

    def test_status_active(self):
        assert _mechanism()["status_check_sep2026"]["status"].startswith("ACTIVE")

    def test_gradient_meta_payer_present(self):
        gradient = _mechanism()["asymmetry_relevance"]["gradient"]
        assert "Meta-payer PRESENT" in gradient

    def test_tone_predictor_moderate_weak_and_no_tone_claim(self):
        ar = _mechanism()["asymmetry_relevance"]
        assert ar["tone_predictor_grade"] == "MODERATE-WEAK"
        assert ar["no_tone_claim"] is True

    def test_falsification_membership_seventeenth(self):
        ff = _mechanism()["falsification_family"]
        assert "SEVENTEENTH" in ff["membership"]
        assert "ledger stood at 16 after #688" in ff["membership"]

    def test_falsification_prediction_and_observed(self):
        ff = _mechanism()["falsification_family"]
        assert "Prisa" in ff["prediction"]
        assert "toxic spills" in ff["observed"]
        assert "$18 billion" in ff["observed"]

    def test_illustrative_tone_minus_055(self):
        assert "-0.55" in _mechanism()["falsification_family"]["illustrative_tone"]

    def test_second_meta_payer_pin(self):
        ff = _mechanism()["falsification_family"]
        assert "second falsification pin where Meta is the payer leg" in ff["second_meta_payer_pin"]
        assert "#664" in ff["second_meta_payer_pin"]

    def test_corroborating_le_monde_pin_is_weaker(self):
        ff = _mechanism()["falsification_family"]
        assert "WEAKER pin" in ff["corroborating_lemonade_pin"]
        assert "corroborating only" in ff["corroborating_lemonade_pin"]

    def test_cross_outlet_nuance_three_counterparties(self):
        nuance = _mechanism()["falsification_family"]["cross_outlet_nuance"]
        for name in ("Bobrowsky", "Katie Paul", "El Pais"):
            assert name in nuance, f"cross-outlet voice missing: {name}"
        assert "Payment direction alone does not determine register" in nuance

    def test_ranked_confounders_six(self):
        confs = _mechanism()["ranked_confounders"]
        assert len(confs) == 6
        strengths = [c["strength"] for c in confs]
        assert strengths.count("strong") == 3
        assert strengths.count("moderate") == 2
        assert strengths.count("weak") == 1

    def test_settlement_confounder_leads(self):
        c1 = _mechanism()["ranked_confounders"][0]
        assert c1["rank"] == 1
        assert c1["strength"] == "strong"
        assert "$18B" in c1["confounder"]

    def test_counterevidence_three_entries(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 3


class TestCrossReferences689:
    def test_newscorp_549_sibling_leg_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 549" in refs

    def test_reuters_633_first_payer_pin_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 633" in refs
        assert "#664" in refs

    def test_662_and_688_family_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "#662" in refs
        assert "#688" in refs

    def test_grade_comparators_684_679_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "#684" in refs
        assert "#679" in refs

    def test_conventions_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "#599" in refs
        assert "#492" in refs

    def test_standing_rule_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "Aug 28 2026 standing rule" in refs

    def test_llm_pulse_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "LLM Pulse" in refs

    def test_distinct_from_549_and_633(self):
        nov = " ".join(_mechanism()["novelty_verification"])
        assert "mechanism 549" in nov
        assert "mechanism 633" in nov


class TestNovelty689:
    def test_single_689_file_on_disk(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_689*"))
        assert files == [os.path.join(TESTS_DIR, FILENAME)], files

    def test_no_duplicate_648_mechanism_key(self):
        count = 0
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path).read()
            count += len(re.findall(r"^    mechanism_648_meta_european", text, re.M))
        assert count == 1, f"mechanism_648 key appears {count} times"

    def test_no_prior_dedicated_european_bundle_mechanism(self):
        # Prior mentions are the LLM Pulse lines inside mechanism_633's
        # cross-references. No prior block names a Meta x European
        # publishers bundle deal-level leg.
        # (Parsed via YAML, not raw-text regex: the mechanism_name carries
        # ''-escaped apostrophes that truncate a naive '[^']*' capture.)
        names = []

        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if isinstance(k, str) and k.startswith("mechanism_") and isinstance(v, dict):
                        nm = v.get("mechanism_name")
                        if isinstance(nm, str) and "European" in nm:
                            names.append(nm)
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)

        walk(_entities())
        dedicated = [n for n in names if "European Publishers Bundle" in n]
        assert dedicated == [_mechanism()["mechanism_name"]], dedicated

    def test_elpais_url_new_to_corpus_pin(self):
        nov = " ".join(_mechanism()["novelty_verification"])
        assert "El Pais Aug 30 2026 toxic-spills URL zero repo-wide hits pre-commit" in nov

    def test_seventeenth_novelty(self):
        nov = " ".join(_mechanism()["novelty_verification"])
        # The SEVENTEENTH claim is pinned in the falsification block, not
        # re-asserted here; this test pins the membership field exists.
        assert "SEVENTEENTH" in _mechanism()["falsification_family"]["membership"]


class TestResearchMethod689:
    def test_mechanism_key_naming(self):
        assert MECH_KEY.startswith("mechanism_648_")
        assert MECH_KEY in _meta()

    def test_no_em_dash_or_curly_quotes_in_mechanism(self):
        text = _mechanism_text()
        assert "\u2014" not in text, "em dash found in mechanism block"
        assert "\u2018" not in text and "\u2019" not in text, "curly quote in mechanism block"

    def test_mechanism_text_ascii_only(self):
        text = _mechanism_text()
        bad = [c for c in text if ord(c) > 127]
        assert not bad, f"non-ASCII chars in mechanism block: {set(bad)!r}"

    def test_type_c_689_main_commit_unique_and_anchored(self):
        # Novelty anchor: exactly one "Type C #689:" main commit post-followup
        # (deselected pre-commit per the #565 convention; the followup and
        # doc-sync commits are "Type C #689 followup:" / "Type C #689
        # doc-sync:" and do NOT match the main-commit filter).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type C #689:", l)]
        assert len(mains) == 1, f"expected exactly one Type C #689 main commit, got {len(mains)}"
        assert mains[0].startswith(ANCHORED_SHA), (
            f"main commit SHA does not match patched anchor: {mains[0][:12]}"
        )

    def test_all_source_urls_present(self):
        urls = _mechanism()["source_urls"]
        for u in (ABOUTFB_URL, SEEKINGALPHA_URL, ELOUTPUT_URL, ABIT_URL,
                  ENGADGET_URL, EP_URL, ELPAIS_URL, LEMONDE_URL, LLMPULSE_URL):
            assert u in urls, f"source URL missing: {u[:60]}"

    def test_research_method_names_query_sets(self):
        rm = _mechanism()["research_method"]
        assert "3 browser.search query sets" in rm

    def test_excerpt_bounded_disclosed(self):
        rm = _mechanism()["research_method"]
        assert "excerpt-bounded" in rm
        assert "not opened first-hand this run" in rm

    def test_no_canonical_urls_constructed(self):
        assert "no canonical URLs constructed" in _mechanism()["research_method"]

    def test_bounded_absence_discipline(self):
        assert "iteration-492 rule" in _mechanism()["research_method"]

    def test_precommit_novelty_greps_documented(self):
        rm = _mechanism()["research_method"]
        assert "zero test_type_c_689 files on disk" in rm
        assert "max numeric mechanism id pre-commit 647" in rm


class TestStatisticalDiscipline689:
    def test_no_scorer_run(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"

    def test_tone_scores_not_scored(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_qualitative_only(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True

    def test_correlational_note_names_moderate_weak_grade(self):
        ar = _mechanism()["asymmetry_relevance"]
        assert ar["tone_predictor_grade"] == "MODERATE-WEAK"
        assert "why_moderate_weak" in ar

    def test_verification_block(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["is_significant"] is False
        assert sd["artifact_grade"] is False


class TestRotationCycleGuard689:
    @staticmethod
    def _distinct_mains(limit=5):
        # First occurrence of each distinct iteration number, newest first.
        # Robust to the followup/doc-sync SHA-fix history: followup commits
        # titled "Type C #689 followup: ..." match the main-commit filter,
        # so raw subjects show repeats. Distinct numbering is the intent.
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen_nums = set()
        mains = []
        for s in out:
            if not re.match(r"^Type [A-E] #\d+:", s):
                continue
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            if m.group(2) in seen_nums:
                continue
            seen_nums.add(m.group(2))
            mains.append((m.group(1), m.group(2)))
            if len(mains) == limit:
                break
        return mains

    def test_window_685_689_closes_b_to_c(self):
        observed = self._distinct_mains(5)
        assert observed == [
            ("C", "689"),
            ("B", "688"),
            ("A", "687"),
            ("E", "686"),
            ("D", "685"),
        ], f"rotation window 685-689 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        observed = [t for t, _ in self._distinct_mains(5)]
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #689 main commit. Patched in the followup
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
        assert subject.startswith("Type C #689:"), (
            f"post-commit anchor broken: newest main is not #689: {subject!r}"
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
        sample = "Type C #689: Meta x European Publishers Bundle March 2026 AI news licensing deal"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "C" and m.group(2) == "689", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet689:
    def test_readme_has_689_row(self):
        assert "#689" in read_readme()

    def test_arch_has_689_row(self):
        assert "689" in read_arch()

    def test_readme_row_mentions_european_publishers(self):
        assert "European" in read_readme()
        assert "Prisa" in read_readme()

    def test_log_starts_with_689(self):
        assert read_log_start().startswith("#689 Type C:")

    def test_def_test_count_matches(self):
        # The README row for #689 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #689 row should mention this file's def-test count {n}"
        )


class TestNoBrittlePatterns689:
    def test_yaml_reparses_clean(self):
        m = _mechanism()
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["iteration"], int)
        assert isinstance(m["ranked_confounders"], list)

    def test_mechanism_key_format(self):
        assert MECH_KEY == "mechanism_648_meta_european_publishers_bundle_mar2026"

    def test_source_urls_all_https(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("https://"), f"non-https source URL: {u}"
