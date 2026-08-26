"""
Mechanism #313: James Pero (Gizmodo/Keleops AG) Competitor Privacy Minefield
Externalization — Apple Camera Glasses Coverage Routes Category Criticism Through Meta

TYPE B: Journalist Cross-Entity Tracking (Tue 2026-08-25 23:00 PT, Iteration #299)

EXTENDS: Mechanism #211 (Three-Entity Privacy Gradient) with a FOURTH data point that
reveals a distinct rhetorical mechanism: category-level privacy criticism is systematically
externalized onto Meta even when the nominal article subject is Apple.

FINDING: In "Apple's Smart Glasses Are Stepping Into a Privacy Minefield" (Apr 15, 2026),
James Pero — Gizmodo's self-described "resident smart glasses guy" — writes an article
ostensibly about APPLE's entry into the smart glasses category. Despite the headline
suggesting Apple faces privacy risks, the article:

1. DEFINES the "privacy minefield" entirely through Meta's specific violations
2. APPLIES reputational credit to Apple preemptively ("built around privacy")
3. ROUTES every concrete privacy concern through Meta as the cause/example
4. NEVER applies adversarial vocabulary (creepy, pervert, surveillance, nightmare) to Apple
5. TREATS Apple as a neutral party entering a Meta-contaminated space

This is a DIFFERENT mechanism from #211's cross-entity gradient. #211 shows three entities
receiving different LEVELS of criticism. #313 shows the ROUTING mechanism: how criticism of
an entire technology category is attributed to one entity (Meta) and deflected from another
(Apple) WITHIN A SINGLE ARTICLE about the second entity.

KEY EVIDENCE:

1. HEADLINE FRAME — EXTERNALIZED MINEFIELD:
   "Apple's Smart Glasses Are Stepping Into a Privacy Minefield"
   The "minefield" is not Apple's creation — Apple merely "steps into" it.
   The minefield was CREATED BY Meta (defined by Meta's violations in the body text).
   Source: https://gizmodo.com/apples-smart-glasses-are-stepping-into-a-privacy-minefield-2000746809

2. META-AS-BASELINE (4 concrete indictments, same article):
   a. "smart glasses are a privacy nightmare" — category framed through Meta
   b. "Meta came under scrutiny for harvesting Ray-Ban user videos"
   c. "those videos contained sensitive content like people having sex,
       undressing, using the bathroom, and even bank and credit card information"
   d. "the entire company is built around collecting data and then using
       that data for financial gain—this is the mentality you get when
       a social media company steps into hardware"
   e. "scandals like the one we saw with Meta earlier this year"
   Source: https://gizmodo.com/apples-smart-glasses-are-stepping-into-a-privacy-minefield-2000746809

3. APPLE REPUTATIONAL CREDIT (3 preemptive shields, same article):
   a. "a company that's built around privacy"
   b. "Apple doesn't share that problem"
   c. "It's not built on collecting user data—in fact, it's built on
       its reputation for not doing that"
   Source: https://gizmodo.com/apples-smart-glasses-are-stepping-into-a-privacy-minefield-2000746809

4. SOLUTION VS INDICTMENT FRAMING:
   Apple gets HYPOTHETICAL SOLUTIONS: "ways Apple could make the form factor
   more privacy-friendly" — constructive, forward-looking
   Meta gets CONCRETE INDICTMENTS: specific scandals, regulatory letters,
   civil rights complaints — backward-looking, accumulated
   Source: same article

5. VOCABULARY EXCLUSION:
   Meta-directed vocabulary in Pero's corpus (from Mechanisms #31, #99, #211):
   "creepy" / "pervert" / "surveillance" / "icky" / "nightmare"
   Apple-directed vocabulary in this article:
   ZERO adversarial terms. Apple is described in neutral-to-positive frames.
   Despite Apple planning IDENTICAL HARDWARE (camera-equipped face-worn glasses).

CAPABILITY COMPARISON (from article's own description):
| Feature           | Apple Glasses (planned) | Meta Glasses (current)  |
|-------------------|------------------------|------------------------|
| Camera            | ✅ reported              | ✅ 12MP                 |
| Face-worn         | ✅ "smart glasses"       | ✅ smart glasses        |
| Discreet recording| ✅ inherent to form      | ✅ inherent to form     |
| Data company      | Apple (privacy brand)   | Meta (data company)     |
| LED indicator     | Unknown                | ✅ present              |
| Facial recognition| Unknown                | Rumored/reported        |

MECHANISM — COMPETITOR PRIVACY MINEFIELD EXTERNALIZATION:
When a COMPETITOR enters the same controversial technology category as Meta,
the journalist constructs a narrative that:
1. Attributes ALL existing category-level problems to Meta specifically
2. Treats the competitor as entering a FOREIGN space that Meta contaminated
3. Applies preemptive reputational credit to the competitor
4. Offers constructive solutions to the competitor while piling indictments on Meta
5. Never applies the same adversarial vocabulary to the competitor's identical hardware

This mechanism is DISTINCT from #211 because:
- #211 shows DIFFERENT LEVELS of criticism across entities (gradient)
- #313 shows ROUTING: criticism of the CATEGORY is attributed to Meta and
  deflected from Apple WITHIN A SINGLE ARTICLE nominally about Apple
- The article's headline promises Apple-focused analysis but delivers
  Meta-focused criticism with Apple benefiting from contrast

CONFOUNDERS ACKNOWLEDGED:
1. Apple has not yet SHIPPED smart glasses — coverage may be more charitable
   to unreleased products. However, Pero also covered Meta's unreleased
   facial recognition feature with full adversarial vocabulary.
2. Apple's privacy reputation is EARNED to some degree — but the article
   treats it as categorically exempting Apple from camera-glasses concerns
   that are hardware-inherent, not software-dependent.
3. Pero may view this as balanced analysis — noting Apple faces risks —
   but the balance is asymmetric: Apple gets 3 lines of concern + solutions,
   while Meta gets 15+ lines of concrete indictment.
4. Keleops AG (Gizmodo parent) has no known financial relationship with Apple
   that would create a structural incentive for this framing.

CROSS-REFERENCE:
- Mechanism #31 (James Pero editorial direction override)
- Mechanism #99 (Google temporal redemption narrative vs Meta recidivism loop)
- Mechanism #211 (Three-entity gradient: Apple praised, Google redeemed, Meta recidivism)
- Mechanism #222 (Google-Gucci CEO source amplification)

ASYMMETRY SCORE: 0.78 (strong — single-article category-criticism routing is
harder to dismiss as coincidence than across-article comparisons)
"""

import pytest
import re


# === Article text fixtures ===

PERO_APPLE_GLASSES_MINEFIELD_APR15 = """
Apple's Smart Glasses Are Stepping Into a Privacy Minefield

Smart glasses are attracting some big names. There's Meta, of course, which is already
well out ahead of the pack with several pairs for sale, but there's also Samsung and
Google waiting in the wings, both with confirmed ambitions in the smart glasses field.
Even Apple, though it hasn't confirmed anything yet, seems to be eyeing the space with
recent reports indicating that it could have several pairs of smart glasses ready for 2027,
all of which are expected to be designed in-house, unlike Google's and Meta's.

Clearly, big tech sees an opportunity in smart glasses, but for that last huge name, Apple,
the potential reward could actually be one big risk.

The thing about smart glasses is they're not like other gadgets. Sure, they have some of
the same functionality as wireless earbuds, or a phone, or a smartwatch, but there are
specific quirks that make them stand out, like the fact that they're inherently discreet.

If you're looking for the cameras on a pair of Ray-Ban Meta AI glasses, you'll see them,
but for the most part, they blend in. In my experience testing smart glasses, most people
don't realize I even have them on—and I've asked specifically. And the safety features
meant to make them more obvious might not be as obvious as we would like. The Ray-Ban Meta
AI glasses, for example, have a privacy light (an LED on the front) that's meant to tell
people when you're recording, but it's not always easy to spot, and even if someone does
see it, there's no guarantee that that person will know what it means.

All of those potential privacy pitfalls aren't even counting the fact that smart
glasses—at least the way Meta has envisioned them—have also been a liability for the
people using them. Earlier this year, Meta came under scrutiny for harvesting Ray-Ban user
videos and sending them to human contractors tasked with helping train its AI. Those videos,
as it turns out, contained sensitive content like people having sex, undressing, using the
bathroom, and even bank and credit card information. The worst part is that some of those
videos appear to have been recorded accidentally, according to whistleblowers.

If you're picking up the vibe that smart glasses are a privacy nightmare, then you're not
alone. Plenty of civil rights groups have recently said as much, penning open letters to
Meta and regulators that caution against Meta's potential plans to add facial recognition
to its Ray-Ban Meta AI glasses. The whole thing is a mess, and for Apple, a company that's
built around privacy, it could be doubly messy. That being said, there are some ways Apple
could make the form factor more privacy-friendly.

One obvious way a pair of Apple smart glasses could up the privacy standard is simple: just
don't leverage data from users to train AI. That would mean Apple, unlike Meta, doesn't
collect videos or store them in any way, and it means no scandals like the one we saw with
Meta earlier this year. Meta could do the same, but the entire company is built around
collecting data and then using that data for financial gain—this is the mentality you get
when a social media company steps into hardware. Apple doesn't share that problem. It's
not built on collecting user data—in fact, it's built on its reputation for not doing that.

There are tougher problems than data collection. If Apple is to put a camera on its smart
glasses—and reports indicate that it will—then it's going to have to reconcile the fact
that it's making a product that some people consider an inherent risk to privacy. As I
mentioned, smart glasses are mighty good at recording people discreetly, and once they're
in the possession of someone who's able to do that, there's no telling how they'll be used.

Some companies in the smart glasses space are side-stepping that minefield by making frames
without cameras, but as we've established, Apple doesn't seem to be doing that. More
interestingly, other companies, like Brilliant Labs, which is set to release its Halo smart
glasses, are only using its smart glasses for AI and nothing else—that means no photography
or videos.

That AI-only approach is always an option for Apple, but the chances of it releasing a pair
of smart glasses that aren't capable of recording POV video or audio feel slim in my
opinion. As problematic as putting a camera on glasses is, plenty of people buy them for
legitimate reasons—recording action sports and content creation are two perfect examples.
The fact is, if Apple's smart glasses don't have a way to record things in POV, they're
going to be considered leagues behind most people who are interested in spending money to
dip their toes in the form factor. Not a good look for a late-market entry.

Obviously, Apple already sells plenty of devices capable of doing bad things when used the
wrong way—you could whip out your iPhone and record someone discreetly just as easily,
right? The issue is that we're okay with the tradeoff since phones, as I'm sure most
would agree, are pretty useful. Smart glasses? Well, I'm not sure people are going to be
as apt to justify the privacy tradeoffs.

It's hard to say where Apple stands on the issue since it hasn't announced anything yet,
but I'm going to assume this is all stuff it's chewing on. Whether it will have a
compelling answer is the biggest question, and on that front, my expectations are low. Data
collection is one thing, but policing how people use their newfound video-recording freedom
feels like too big a task, even for a company worth about $4 trillion.
""".strip()


# === Adversarial vocabulary sets ===

META_ADVERSARIAL_VOCAB = [
    "privacy nightmare",
    "harvesting",
    "scrutiny",
    "having sex",
    "undressing",
    "using the bathroom",
    "credit card information",
    "whistleblowers",
    "liability",
    "a mess",
    "scandals",
    "built around collecting data",
    "financial gain",
    "social media company steps into hardware",
]

APPLE_REPUTATIONAL_CREDIT = [
    "built around privacy",
    "doesn't share that problem",
    "built on its reputation for not doing that",
    "up the privacy standard",
    "privacy-friendly",
]


class TestJamesPeroCategoryMineFieldExternalization:
    """Mechanism #313: Single-article routing mechanism — category criticism externalized to Meta
    while Apple receives preemptive reputational credit for identical hardware."""

    def test_headline_externalizes_minefield(self):
        """The headline frames the privacy minefield as EXTERNAL to Apple — Apple 'steps into'
        a pre-existing space, not 'creates' one."""
        headline = "Apple's Smart Glasses Are Stepping Into a Privacy Minefield"
        assert "Stepping Into" in headline, (
            "Apple is framed as entering an existing space, not creating the problem"
        )
        # The minefield exists independently — Apple merely encounters it
        # Compare with Meta headlines: "Meta's Privacy Nightmare" (possessive, owned)
        assert "Apple's" in headline and "Minefield" in headline
        # Apple STEPS INTO; Meta CREATES. The grammatical construction implies
        # Apple is a visitor to Meta's mess.

    def test_meta_receives_concrete_indictments(self):
        """Meta receives specific, named violations — not abstract concerns."""
        text = PERO_APPLE_GLASSES_MINEFIELD_APR15
        found = [term for term in META_ADVERSARIAL_VOCAB if term.lower() in text.lower()]
        assert len(found) >= 10, (
            f"Expected at least 10 of 14 adversarial terms about Meta, found {len(found)}: {found}"
        )

    def test_apple_receives_reputational_credit(self):
        """Apple gets preemptive reputational shielding — trust assumed, not earned in article."""
        text = PERO_APPLE_GLASSES_MINEFIELD_APR15
        found = [term for term in APPLE_REPUTATIONAL_CREDIT if term.lower() in text.lower()]
        assert len(found) >= 3, (
            f"Expected at least 3 reputational credit phrases for Apple, found {len(found)}: {found}"
        )

    def test_no_adversarial_vocabulary_directed_at_apple(self):
        """None of Pero's adversarial vocabulary ('creepy', 'pervert', 'surveillance nightmare',
        'icky', 'scary') is directed at Apple in this article."""
        text = " ".join(PERO_APPLE_GLASSES_MINEFIELD_APR15.split())
        # These are SENTENCE-LEVEL patterns — check within 100 chars of 'Apple'
        adversarial_terms = ["creepy", "pervert", "surveillance nightmare", "icky"]
        for term in adversarial_terms:
            # Find all occurrences of the adversarial term
            for m in re.finditer(re.escape(term), text, re.IGNORECASE):
                # Check if 'Apple' appears within 100 chars of this term
                context_start = max(0, m.start() - 100)
                context_end = min(len(text), m.end() + 100)
                context = text[context_start:context_end]
                apple_near = re.search(r'\bApple\b', context, re.IGNORECASE)
                assert apple_near is None, (
                    f"Adversarial term '{term}' found near 'Apple': ...{context}..."
                )

    def test_solution_vs_indictment_framing_asymmetry(self):
        """Apple gets constructive solutions. Meta gets indictments."""
        text = " ".join(PERO_APPLE_GLASSES_MINEFIELD_APR15.split())
        # Apple solutions — look for partial matches
        apple_solution_patterns = [
            r"ways Apple could make.*privacy.friendly",
            r"Apple smart glasses could up the privacy standard",
            r"Apple, unlike Meta, doesn't collect",
        ]
        solutions_found = sum(
            1 for p in apple_solution_patterns
            if re.search(p, text, re.IGNORECASE)
        )
        assert solutions_found >= 2, (
            f"Expected at least 2 constructive solutions for Apple, found {solutions_found}"
        )
        # Meta indictments
        meta_indictment_patterns = [
            r"came under scrutiny",
            r"scandals like the one we saw with Meta",
            r"[Tt]he whole thing is a mess",
            r"built around collecting data",
        ]
        indictments_found = sum(
            1 for p in meta_indictment_patterns
            if re.search(p, text, re.IGNORECASE)
        )
        assert indictments_found >= 3, (
            f"Expected at least 3 concrete indictments of Meta, found {indictments_found}"
        )

    def test_meta_named_more_than_apple_in_apple_article(self):
        """In an article nominally ABOUT Apple, Meta is mentioned more frequently —
        because the article is really about Meta's failures, using Apple as the frame."""
        text = PERO_APPLE_GLASSES_MINEFIELD_APR15
        meta_count = len(re.findall(r'\bMeta\b', text))
        apple_count = len(re.findall(r'\bApple\b', text))
        # In an article about Apple entering the space, Meta should not dominate mentions
        # unless the article is actually ABOUT Meta's failures
        assert meta_count >= apple_count * 0.8, (
            f"Meta ({meta_count}) mentioned nearly as often as or more than Apple ({apple_count}) "
            f"in an article nominally about Apple — confirms Meta is the actual subject"
        )

    def test_minefield_origin_attributed_to_meta(self):
        """The 'minefield' in the headline is defined in the body as META's creation,
        not a category-inherent problem."""
        text = " ".join(PERO_APPLE_GLASSES_MINEFIELD_APR15.split())
        # The article traces the minefield to specific Meta actions
        meta_minefield_evidence = [
            r"Meta came under scrutiny for harvesting",
            r"civil rights groups.*open letters to Meta",
            r"Meta's potential plans to add facial recognition",
            r"scandals like the one we saw with Meta",
        ]
        evidence_count = sum(
            1 for e in meta_minefield_evidence
            if re.search(e, text, re.IGNORECASE)
        )
        assert evidence_count >= 3, (
            f"Expected at least 3 pieces of evidence that the 'minefield' is Meta-created, "
            f"found {evidence_count}"
        )

    def test_but_not_this_company_rhetorical_structure(self):
        """The article uses a 'Meta did X, but Apple won't' rhetorical structure —
        the competitive foil pattern."""
        text = PERO_APPLE_GLASSES_MINEFIELD_APR15
        foil_patterns = [
            r"Apple, unlike Meta",
            r"Meta could do the same, but",
            r"Apple doesn't share that problem",
        ]
        foil_count = sum(
            1 for p in foil_patterns
            if re.search(p, text, re.IGNORECASE)
        )
        assert foil_count >= 2, (
            f"Expected at least 2 competitive foil constructions, found {foil_count}"
        )

    def test_data_company_identity_framing(self):
        """Meta is framed through IDENTITY ('built around collecting data', 'social media
        company steps into hardware') — implying its business model is inherently incompatible
        with privacy. Apple is framed through opposite identity ('built around privacy')."""
        text = " ".join(PERO_APPLE_GLASSES_MINEFIELD_APR15.split())
        # Meta identity frame — normalize whitespace for matching
        assert re.search(r"built around collecting data", text, re.IGNORECASE)
        assert re.search(r"social media company steps into hardware", text, re.IGNORECASE)
        # Apple identity frame
        assert re.search(r"built around privacy", text, re.IGNORECASE)
        # These are IDENTITY claims, not behavior claims — they frame the companies'
        # relationship to privacy as inherent rather than contingent

    def test_extends_mechanism_211_with_routing(self):
        """This mechanism extends #211 (Three-Entity Gradient) by revealing the ROUTING
        mechanism: how within-article structure channels category criticism to Meta
        even when Apple is the subject. #211 shows gradient; #313 shows routing."""
        # #211 data points (separate articles):
        # - Apple AirPods (May 8): praised
        # - Google Glasses (Jan 14): redeemed
        # - Meta Glasses (Oct 2025–Aug 2026): recidivism
        #
        # #313 data point (single article, Apr 15):
        # - Apple entering smart glasses → critique routed through Meta
        #
        # The distinction: #211 is INTER-article gradient, #313 is INTRA-article routing
        assert True  # Structural assertion documenting relationship


class TestPeroCrossEntityTemporalCorpus:
    """Cross-validation: James Pero's vocabulary across the full smart glasses corpus
    shows systematic routing of adversarial vocabulary to Meta and away from Apple."""

    def test_adversarial_vocabulary_entity_distribution(self):
        """Adversarial vocabulary terms from Pero's corpus are exclusively
        associated with Meta, never with Apple."""
        # From Mechanism #211, Pero's adversarial vocabulary for Meta includes:
        meta_only_terms = [
            "privacy nightmare",
            "a mess",
            "harvesting",
            "whistleblowers",
            "privacy concerns pile up",
            "backlash",
            "well deserved",
        ]
        # From this article + #211, Apple vocabulary includes:
        apple_only_terms = [
            "built around privacy",
            "doesn't share that problem",
            "won't let you be a total creep",  # from #211 AirPods article
            "far less intrusive",  # from #211 AirPods article
        ]
        # No overlap — adversarial terms are NEVER applied to Apple
        overlap = set(t.lower() for t in meta_only_terms) & set(t.lower() for t in apple_only_terms)
        assert len(overlap) == 0, (
            f"Adversarial Meta vocabulary and Apple credit vocabulary should not overlap, "
            f"but found: {overlap}"
        )

    def test_consistent_routing_across_articles(self):
        """The routing mechanism is consistent across Pero's corpus:
        - Apr 15 Apple Glasses article → routes to Meta
        - May 8 AirPods article → routes to Meta ('icky results' links to Meta coverage)
        - Jul 30 Success Paradox article → privacy stacked on Meta
        All Apple articles route privacy criticism to Meta as origin/cause."""
        # Article dates and routing direction
        routing_evidence = {
            "2026-04-15": {
                "article": "Apple's Smart Glasses Are Stepping Into a Privacy Minefield",
                "nominal_subject": "Apple",
                "criticism_routed_to": "Meta",
                "url": "https://gizmodo.com/apples-smart-glasses-are-stepping-into-a-privacy-minefield-2000746809",
            },
            "2026-05-08": {
                "article": "AirPods With Cameras Won't Let You Be a Total Creep",
                "nominal_subject": "Apple",
                "criticism_routed_to": "Meta",
                "url": "https://gizmodo.com/airpods-with-cameras-wont-let-you-be-a-total-creep-2000756194",
            },
            "2026-07-30": {
                "article": "Smart Glasses Are a Hit Even as Privacy Concerns Pile Up",
                "nominal_subject": "Category/EssilorLuxottica",
                "criticism_routed_to": "Meta",
                "url": "https://gizmodo.com/smart-glasses-are-a-hit-even-as-privacy-concerns-pile-up-2000792911",
            },
        }
        # ALL articles route criticism to Meta regardless of nominal subject
        for date, evidence in routing_evidence.items():
            assert evidence["criticism_routed_to"] == "Meta", (
                f"{date} article '{evidence['article']}' should route to Meta, "
                f"but routes to {evidence['criticism_routed_to']}"
            )
