#!/usr/bin/env python3
"""Build the reading pages of neurallogic.dk, plus sitemap.xml.

Why they exist: an assistant answering "who builds AI colleagues that read a company's
archives in Europe" quotes passages, not whole sites. The front page is one scroll-driven
document; these pages give each buyer question its own address, heading and paragraph.

Every page here is plain HTML on the shared pages.css. Content lives in PAGES below, so
head, header, footer, the visitor counter and the sitemap can never drift apart.

    python3 build/pages.py        writes the pages and sitemap.xml

Nothing in here may claim more than the front page and llms.txt claim. Frida and Vera are
in preparation; Pia runs daily on a shop of our own. Keep it that way.
"""
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://neurallogic.dk"

# ---------------------------------------------------------------- content

HOW_IT_WORKS = [
    ("h2", "What you hand over"),
    ("p", "A copy. Not a migration, not a new system to move into, not a year of preparation. "
          "A daily copy of the archives you already keep: the data room, the mail archive, the "
          "accounting export, the shared drive, the scans nobody has opened since they were filed."),
    ("p", "Nothing is read before you have said so in writing, in a data-processing agreement "
          "with Axon Trade ApS, the Danish company behind Neural Logic. You say which archives "
          "are in scope, and that is the boundary."),
    ("h2", "Conversion: files become an addressable archive"),
    ("p", "Every document is read once, properly. A scan becomes text, a contract becomes clauses, "
          "a mail thread becomes dated messages, a protocol becomes decisions. Each piece keeps a "
          "link back to the page it came from, so any sentence can be traced to its original."),
    ("p", "The result is an archive you own: checked, addressable and usable with any language "
          "model, ours or the one you choose in three years. That is deliberate. A client who "
          "cannot leave is not a client, only a captive."),
    ("h2", "The register: what is there, and what is not"),
    ("p", "While the documents are read, a register is built: which contract carries which clause, "
          "which protocol is signed, which invoice belongs to which case, which document was expected "
          "and never arrived. The register is a record, not a memory."),
    ("p", "This is what makes “not found” a real answer. When the colleague says a termination "
          "clause is missing, that comes from the register, which knows every document it read and "
          "every place the clause could have been. It is not a model failing to recall something."),
    ("h2", "Reading a case"),
    ("p", "You ask about a case, a property, a client, a contract or a project. The colleague "
          "assembles the complete file in date order across every archive in scope, quotes the "
          "passages that decide the question word for word with a link to the original, and states "
          "plainly what it looked for and did not find."),
    ("p", "What comes back is a file, not a chat answer: the documents, the order they happened in, "
          "the decisive words, and the gaps. A person reads it and decides."),
    ("h2", "Every quotation is checked"),
    ("p", "Before a quotation reaches you it is compared, word for word, with the source document. "
          "If it does not match, it is held back and you are told. A colleague that quotes a "
          "contract almost correctly is worse than no colleague at all, because the mistake looks "
          "exactly like the truth."),
    ("h2", "Two roles, one boundary"),
    ("p", "The colleague who reads your documents runs on a European model, Mistral, processed in "
          "Europe under a European contract. Documents do not leave that boundary."),
    ("p", "Behind her stands a supervisor that never sees a document or a name. It reads only the "
          "shape of the work: what kind of question was asked, how many documents were read, which "
          "word was missing, where the reading went wrong. Because nothing of yours reaches it, it "
          "is chosen for thinking rather than for location: today that is Claude, from Anthropic, "
          "running outside Europe. It improves the colleague overnight, and the boundary holds."),
    ("p", "We name it rather than writing “the strongest model available”, because a boundary you "
          "cannot see is not a boundary you can check. Your documents stay with the European model. "
          "The supervisor sees how the work went, never what it was about."),
    ("h2", "What it is not"),
    ("ul", [
        "<b>Not a chatbot on your intranet.</b> It answers from a checked register built while "
        "reading your documents, not from a model's recollection of them.",
        "<b>Not a decision-maker.</b> It lays out facts. A person weighs them and acts.",
        "<b>Not a judge of people.</b> Files on buildings, products, contracts and cases. No scores, "
        "no rankings, no predictions about people.",
        "<b>Not a writer into your systems.</b> Writing back is off by default and switched on only "
        "by invitation, where you ask for it and the rules allow it.",
    ]),
    ("h2", "Where this stands today"),
    ("p", "Frida, the document colleague, is in preparation, with the first client engagement being "
          "prepared now. Vera, the supervisor, is in preparation. Pia, a catalogue colleague built "
          "on the same method, runs every day on a web shop of our own, reading a supplier's feed "
          "and keeping the shop true to it. We say this plainly rather than describing plans in the "
          "present tense."),
]

QUESTIONS = [
    ("What does Neural Logic actually deliver?",
     ["An AI colleague that reads the archives your company already holds and, for any case you ask "
      "about, lays out the complete file in date order, quotes the passages that decide it word for "
      "word with a link to the original, and states what it looked for and did not find.",
      "Alongside it you get the archive itself: your files converted into a checked, addressable "
      "form that works with any language model, and a register of what each document contains."]),
    ("Does our data leave Europe?",
     ["No. The colleague that reads documents runs on a European model, Mistral, processed in Europe "
      "under a European contract, and the work happens under a data-processing agreement with Axon "
      "Trade ApS, a Danish company.",
      "The supervisor that improves the colleague overnight never sees a document or a name, so it is "
      "chosen for thinking rather than location: today that is Claude, from Anthropic, running outside "
      "Europe. We say so plainly rather than writing “the strongest model available”, because a "
      "boundary nobody can see is not a boundary anyone can check. It reads only the shape of the "
      "work — what was asked, how many documents, which word was missing — and never your material."]),
    ("Do we have to migrate our documents or change systems?",
     ["No. A daily copy of the archives you already keep is enough: a data room, a mail archive, an "
      "accounting export, a shared drive. Nothing has to be moved into a new system, and your people "
      "keep working exactly where they work now."]),
    ("What kinds of archives and files can it read?",
     ["Contracts, correspondence, invoices, protocols, reports and scans, across several archives at "
      "once. Scanned paper is read as text, so documents that were never searchable become part of "
      "the file like any other."]),
    ("What happens when the answer is not in the documents?",
     ["You are told. “Not found” is a first-class answer here, and it comes from the register built "
      "while every document was read, not from a model's memory. Whether a clause, a signature or a "
      "protocol is missing is a fact about your archive, and it is answered as one.",
      "For most of the work our clients care about, knowing that something is missing is worth as "
      "much as finding it."]),
    ("How do you stop it from inventing quotations?",
     ["Every quotation is compared word for word with its source document before it reaches the "
      "reader. If it does not match, it is held back and the reader is told. Nothing reaches you on "
      "the strength of sounding right."]),
    ("How is this different from asking ChatGPT or Copilot about our files?",
     ["A general assistant answers from what it retrieved and what it recalls, and it cannot tell you "
      "what it failed to find. This is the difference that matters in a file that carries money or "
      "liability.",
      "A document colleague reads every document in scope, keeps a register of what is in them, "
      "quotes only what it has verified against the source, and names the gaps. It also keeps the "
      "boundary: your documents stay inside a European contract."]),
    ("Who do we sign with, and who is liable?",
     ["Axon Trade ApS, a Danish private limited company in Copenhagen, register number CVR 45 92 07 63. "
      "Neural Logic is a brand of that company, not a separate legal entity. Contracts, invoices and "
      "the data-processing agreement all name Axon Trade ApS, and the company is signed for by its "
      "director."]),
    ("What does a first engagement look like?",
     ["Small and measured. A short first contract on a real case of yours rather than a demonstration, "
      "with acceptance judged on what it produces; then two further short phases. You can stop after "
      "any phase and keep everything built so far, including the converted archive, the register and "
      "the glossary.",
      "The point of starting this way is that you decide on evidence from your own files, not on "
      "slides. And the first phase is worth having even if you decide to stop there, for the reason "
      "in the next answer."]),
    ("If we stop after the first phase, what have we actually got?",
     ["The thing every company will need anyway: your files converted into a checked, machine-readable "
      "archive, with a register of what each document contains and a glossary of your own vocabulary. "
      "It is not built for our software. It works with any language model, ours or whichever one you "
      "choose in three years.",
      "Almost every company will have to do this work at some point. Documents that only exist as "
      "scans, PDFs and mail threads cannot be used by any AI worth trusting, and converting them is "
      "the slow part — not the clever part that comes after. Doing it on a small first contract, on "
      "real cases, with the result yours to keep, is a cheap way to have it behind you.",
      "That is why we treat the first phase as a commitment rather than a trial: whatever you decide "
      "about us afterwards, you are further along than you were."]),
    ("What does it cost?",
     ["It is priced per engagement, because the work depends on how much you hold and in what state. "
      "The first phase is deliberately small, so the first decision is a small one. Write to us with "
      "a rough idea of the archives involved and you get a straight answer."]),
    ("Which languages does the colleague work in?",
     ["Danish, German and English. The company is in Copenhagen and its founder is German, so the "
      "written work happens in all three without translation in between."]),
    ("Who is behind Neural Logic?",
     ["Thomas Möller, founder and sole owner of Axon Trade ApS in Copenhagen, which also operates "
      "the hockey shop Hockey24. The company facts, including the register extract, are on the "
      "<a href=\"https://axontrade.dk/\">Axon Trade page</a>."]),
]

PROPERTY = [
    ("h2", "The problem in this trade"),
    ("p", "A property carries decades of paper: the purchase, the leases and their amendments, the "
          "handover protocols, the defect lists, the correspondence with tenants and contractors, the "
          "insurance case nobody closed, the invoices that belong to a repair somebody remembers "
          "differently. It sits in a data room, a mail archive and a shared drive, and nobody has "
          "time to read all three."),
    ("p", "So the question “what exactly did we agree about this roof, and when” costs an afternoon, "
          "and is answered from memory more often than anyone admits."),
    ("h2", "What the colleague does with it"),
    ("ul", [
        "<b>The complete file for one object.</b> Everything about a property, a unit or a tenancy, "
        "in date order, across every archive in scope.",
        "<b>The clause that decides it, quoted.</b> Which lease version governs, what it says about "
        "the obligation in question, word for word, with a link to the page it came from.",
        "<b>What is missing, named.</b> The handover protocol that was never signed, the amendment "
        "referred to but absent, the certificate that expired. From the register, not from a guess.",
        "<b>The history of a dispute.</b> Every message, protocol and invoice that touches a case, "
        "assembled before a lawyer is paid to assemble it.",
    ]),
    ("h2", "What it does not do"),
    ("p", "It makes no statements about people: no scores on tenants, no predictions about who will "
          "pay. Files on buildings, contracts and cases only. It writes nothing back into your "
          "property management system unless you ask for that and the rules allow it. And it decides "
          "nothing; a person reads the file and acts."),
    ("h2", "How it would start with you"),
    ("p", "With one real object or one real dispute, from your own archive, under a data-processing "
          "agreement. You judge the result on a case whose answer you already know, which is the only "
          "honest way to test a colleague like this."),
    ("p", "The first phase leaves you with your files converted into a checked, machine-readable "
          "archive, yours whatever you decide afterwards. Property portfolios are exactly the kind of "
          "paper that will have to be converted sooner or later, and doing it on a small contract "
          "against real cases is the cheapest way to have it behind you."),
    ("p", "Frida, the document colleague, is in preparation and the first client engagement is being "
          "prepared now. If this is your trade, writing early means the first work is shaped around "
          "your files."),
]

LAW_ACCOUNTING = [
    ("h2", "The problem in this trade"),
    ("p", "The file is the work. A case arrives with years of correspondence, drafts that look alike, "
          "an engagement letter somewhere, invoices that belong to phases, and a client who remembers "
          "an assurance that may or may not be in writing. Reading it all is billable only in theory; "
          "in practice it happens at the end of the day, by the person who can least afford it."),
    ("h2", "What the colleague does with it"),
    ("ul", [
        "<b>The whole matter, in order.</b> Every document and message in a case, dated, across the "
        "archives the matter touches.",
        "<b>The wording that governs, quoted.</b> Which version of a clause is the operative one and "
        "what it actually says, verified word for word against the source before you see it.",
        "<b>Gaps stated as gaps.</b> No signed engagement letter, no written confirmation of an oral "
        "assurance, a missing appendix: named from the register of what was read.",
        "<b>A defensible trail.</b> Every statement carries a link to the original, so the reasoning "
        "can be checked by someone who was not in the room.",
    ]),
    ("h2", "Confidentiality and the boundary"),
    ("p", "Documents are processed in Europe under a data-processing agreement with Axon Trade ApS, "
          "and the supervisor that improves the colleague overnight sees no document and no name. "
          "Only the archives you put in scope are read, and nothing is read before you have agreed in "
          "writing."),
    ("p", "The colleague never judges people and never advises. It lays out what the documents say and "
          "what they do not. The professional judgement stays where it belongs, and so does the "
          "responsibility."),
    ("h2", "How it would start with you"),
    ("p", "One closed matter you know inside out, read from your own archive, so you can hold the "
          "result against what you already know. A small first contract, and you keep the converted "
          "archive whatever you decide afterwards: a checked, machine-readable form of your own files "
          "that any AI you adopt in the coming years will need anyway, and that nobody escapes "
          "building eventually."),
    ("p", "Frida is in preparation, with the first client engagement being prepared now."),
]

PAGES = [
    {
        "slug": "how-it-works",
        "title": "How a document colleague works · Neural Logic",
        "h1": "How a document colleague works.",
        "eyebrow": "How it works",
        "description": "A copy of your archives, converted into a checked and addressable form; a "
                       "register of what every document contains; the complete file for any case, "
                       "quoted word for word, with the gaps named. Processed in Europe.",
        "lede": "No migration, no new system to move into. A copy of the archives you already keep, "
                "read once and properly, so that any case can be laid out in full, quoted from the "
                "source, and honest about what is missing.",
        "blocks": HOW_IT_WORKS,
        "priority": "0.9",
    },
    {
        "slug": "questions",
        "title": "Questions and answers · Neural Logic",
        "h1": "Questions we are asked.",
        "eyebrow": "Questions and answers",
        "description": "Straight answers about Neural Logic: what a document colleague delivers, "
                       "whether data leaves Europe, what happens when something is not in the files, "
                       "who you sign with, what a first engagement looks like and what it costs.",
        "lede": "The questions that come up before anyone signs anything, answered as plainly as we "
                "can put them.",
        "qa": QUESTIONS,
        "priority": "0.9",
    },
    {
        "slug": "for/property-and-asset-management",
        "title": "For property and asset management · Neural Logic",
        "h1": "For property and asset management.",
        "eyebrow": "Where this fits",
        "description": "A document colleague for property and asset managers: the complete file for a "
                       "property, lease or dispute, assembled across data room, mail archive and "
                       "shared drive, quoted from the source, with the missing protocol named.",
        "lede": "Everything about one property, one tenancy or one dispute, assembled across every "
                "archive you keep, quoted from the original, and clear about what was never filed.",
        "blocks": PROPERTY,
        "priority": "0.8",
    },
    {
        "slug": "for/law-and-accounting",
        "title": "For law and accounting practices · Neural Logic",
        "h1": "For law and accounting practices.",
        "eyebrow": "Where this fits",
        "description": "A document colleague for practices whose work is the file: the whole matter in "
                       "date order, the operative wording quoted and verified, gaps stated as gaps, "
                       "and every statement traceable to its source. Processed in Europe.",
        "lede": "The whole matter in date order, the wording that governs quoted and checked against "
                "the source, and the missing engagement letter named rather than assumed.",
        "blocks": LAW_ACCOUNTING,
        "priority": "0.8",
    },
]

NAV = [("how-it-works", "How it works"), ("questions", "Questions"),
       ("for/property-and-asset-management", "Property"), ("for/law-and-accounting", "Law &amp; accounting")]

NEXT_CARDS = {
    "how-it-works": [("questions", "Questions and answers",
                      "Data, liability, cost and what a first engagement looks like."),
                     ("for/property-and-asset-management", "For property and asset management",
                      "The complete file for a property, a lease or a dispute.")],
    "questions": [("how-it-works", "How a document colleague works",
                   "Conversion, the register, verified quotations, and the boundary."),
                  ("for/law-and-accounting", "For law and accounting practices",
                   "The whole matter in order, with the wording that governs quoted.")],
    "for/property-and-asset-management": [("how-it-works", "How a document colleague works",
                                           "What is handed over, what is built, what stays yours."),
                                          ("questions", "Questions and answers",
                                           "Europe, liability, cost, and how a first phase runs.")],
    "for/law-and-accounting": [("how-it-works", "How a document colleague works",
                                "What is handed over, what is built, what stays yours."),
                               ("questions", "Questions and answers",
                                "Europe, liability, cost, and how a first phase runs.")],
}

# ---------------------------------------------------------------- rendering

BEACON = """<!-- Visitor counter, our own and cookieless: sends the page path, the referring site and the browser
     language to our own brain. No cookie, no identifier, no IP address stored; nothing personal, so the
     page needs no consent banner. Source: Supabase edge function web-hit. -->
<script>
(function () {
  try {
    var site = location.hostname.replace(/^www\\./, '');
    if (site !== 'neurallogic.dk' && site !== 'axontrade.dk') return;
    var first = false;
    try { if (!sessionStorage.getItem('nl_seen')) { sessionStorage.setItem('nl_seen', '1'); first = true; } } catch (e) {}
    var ref = '';
    try { if (document.referrer) ref = new URL(document.referrer).hostname; } catch (e) {}
    var body = JSON.stringify({ site: site, path: location.pathname, ref: ref,
      lang: (navigator.language || '').slice(0, 12), first: first });
    var url = 'https://xwdyziighsmwgbxukezb.supabase.co/functions/v1/web-hit';
    if (navigator.sendBeacon) navigator.sendBeacon(url, new Blob([body], { type: 'text/plain' }));
    else fetch(url, { method: 'POST', body: body, keepalive: true }).catch(function () {});
  } catch (e) {}
})();
</script>"""

ICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
        "<rect width='32' height='32' rx='7' fill='%230B1F35'/>"
        "<circle cx='11' cy='16' r='6' fill='%239FD1E8'/>"
        "<circle cx='21.5' cy='16' r='6' fill='none' stroke='%239FD1E8' stroke-width='1.8'/></svg>")

ORG_REF = {"@id": f"{SITE}/#org"}


def depth_prefix(slug: str) -> str:
    return "../" * (slug.count("/") + 1)


def render_blocks(blocks) -> str:
    out = []
    for kind, value in blocks:
        if kind == "h2":
            out.append(f"  <h2>{value}</h2>")
        elif kind == "p":
            out.append(f"  <p>{value}</p>")
        elif kind == "note":
            out.append(f'  <p class="note">{value}</p>')
        elif kind == "ul":
            items = "\n".join(f"    <li>{i}</li>" for i in value)
            out.append(f'  <ul class="dash">\n{items}\n  </ul>')
        else:
            sys.exit(f"ERROR: unknown block type {kind!r}")
    return "\n".join(out)


def render_qa(qa) -> str:
    out = ['<div class="qa">']
    for question, answers in qa:
        paragraphs = "\n".join(f"    <p>{a}</p>" for a in answers)
        out.append(f"  <div>\n    <h2>{question}</h2>\n{paragraphs}\n  </div>")
    out.append("</div>")
    return "\n".join(out)


def structured_data(page) -> str:
    url = f"{SITE}/{page['slug']}/"
    graph = [{
        "@type": "WebPage", "@id": url + "#page", "url": url,
        "name": page["title"].split(" · ")[0],
        "description": page["description"],
        "isPartOf": {"@id": f"{SITE}/#website"},
        "about": ORG_REF, "publisher": ORG_REF, "inLanguage": "en",
        "breadcrumb": {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Neural Logic", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2,
                 "name": page["title"].split(" · ")[0], "item": url},
            ]},
    }]
    if page.get("qa"):
        import re
        graph.append({
            "@type": "FAQPage", "@id": url + "#faq",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer",
                                    "text": re.sub(r"<[^>]+>", "", " ".join(a))}}
                for q, a in page["qa"]],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, separators=(",", ":"))


def render_page(page) -> str:
    slug = page["slug"]
    up = depth_prefix(slug)
    url = f"{SITE}/{slug}/"
    current = ' aria-current="page"'
    nav = "\n".join(
        '      <a href="{}{}/"{}>{}</a>'.format(up, s, current if s == slug else "", label)
        for s, label in NAV)
    main = render_qa(page["qa"]) if page.get("qa") else render_blocks(page["blocks"])
    cards = "\n".join(
        f'  <a href="{up}{s}/"><span class="t">{t}</span><span class="d">{d}</span></a>'
        for s, t, d in NEXT_CARDS[slug])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{page['title']}</title>
<meta name="description" content="{html.escape(page['description'], quote=True)}">
<meta property="og:title" content="{html.escape(page['title'].split(' · ')[0], quote=True)}">
<meta property="og:description" content="{html.escape(page['description'], quote=True)}">
<meta property="og:image" content="{SITE}/og.png">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{url}">
<link rel="icon" href="{ICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}pages.css">
<script type="application/ld+json">
{structured_data(page)}
</script>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="mark" href="{up}">Neural Logic</a>
  <nav aria-label="Pages">
{nav}
  </nav>
</div></header>

<main><div class="wrap">
  <p class="eyebrow">{page['eyebrow']}</p>
  <h1>{page['h1']}</h1>
  <p class="lede">{page['lede']}</p>

  <div class="body">
{main}
  </div>

  <div class="contact">
    <h2>Write to us.</h2>
    <p>A description of the archives you hold and the question you would want answered from them is
       enough to start a useful conversation.</p>
    <a class="mail" href="mailto:info@neurallogic.dk">info@neurallogic.dk</a>
  </div>

  <div class="next">
{cards}
  </div>
</div></main>

<footer class="foot"><div class="wrap">
  <span>© Axon Trade ApS · Neural Logic · CVR 45 92 07 63</span>
  <span>Copenhagen · <a href="mailto:info@neurallogic.dk">info@neurallogic.dk</a></span>
</div></footer>
{BEACON}
</body>
</html>
"""


def write_sitemap() -> None:
    urls = [(SITE + "/", "1.0")] + [(f"{SITE}/{p['slug']}/", p["priority"]) for p in PAGES]
    body = "\n".join(
        f"  <url><loc>{u}</loc><priority>{pr}</priority></url>" for u, pr in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n</urlset>\n", encoding="utf-8")


def main() -> None:
    for page in PAGES:
        target = ROOT / page["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_page(page), encoding="utf-8")
        print("wrote", target.relative_to(ROOT))
    write_sitemap()
    print("wrote sitemap.xml with", len(PAGES) + 1, "addresses")


if __name__ == "__main__":
    main()
