"""The archive-conversion page, in English, German and Danish.

Lead's ruling of 20 September 2026: the conversion of a company's archive into a
machine-readable form is sold as a thing of its own, because the monthly findability
check found that search returns only tools for it and no company that does the work on
real files. German and Danish get their own page because the German search returns no
vendor of our kind at all, and Denmark is our home market. This narrows, knowingly, the
ruling of 4 September that the site stays English: it applies to this page only.

The three versions say the same things; the German and Danish are written anew from the meaning
under mandate M-018 (Decision #281), never sentence by sentence. If one changes in substance, change all three.
"""

# --------------------------------------------------------------------- English

CONVERSION_EN = [
    ("h2", "The work nobody has done yet"),
    ("p", "A PDF is an electronic document, not a machine-readable one. Neither is a scan, a mail "
          "thread or a folder named “final_v3”. They are readable by people, and opaque to "
          "everything else."),
    ("p", "This is why AI projects in companies with real archives stall. The models are fine. The "
          "material is not: it has no structure, no addresses, no way to say which clause sits in "
          "which version of which contract. Anything built on top of it is guesswork wearing a "
          "confident tone."),
    ("h2", "What conversion actually is"),
    ("p", "Your archive is read once, properly. A scan becomes text. A contract becomes clauses. A "
          "mail thread becomes dated messages with their attachments. A protocol becomes decisions. "
          "Every piece keeps a link back to the page it came from, so any sentence can be traced to "
          "its original."),
    ("p", "While that happens, two things are written down: a register of what each document "
          "contains — and what was expected and never arrived — and a glossary of your own "
          "vocabulary, the words your trade and your company use for things."),
    ("h2", "What you get, and keep"),
    ("ul", [
        "<b>The converted archive</b>, in open formats, usable by any language model — ours, or the "
        "one you choose in three years.",
        "<b>The register:</b> which document holds which clause, which protocol is signed, which "
        "invoice belongs to which case, and which documents are missing.",
        "<b>Your glossary:</b> the terms your company actually uses, so a machine reading your files "
        "does not have to guess at them.",
        "<b>A written account of what could not be read</b>, and why. Unreadable pages, broken "
        "scans, files that were empty. Most archives contain a few, and nobody knows until someone "
        "reads them all.",
    ]),
    ("p", "All of it is yours, in your hands, not locked in a system of ours. That is not "
          "generosity; a client who cannot leave is not a client, only a captive."),
    ("h2", "Why this is worth doing on its own"),
    ("p", "Whatever you eventually use AI for, and whoever you eventually hire to build it, this "
          "work comes first. It is the slow part, and it does not get cheaper by waiting. Doing it "
          "once, on a small contract, with the result yours to keep, means it is behind you before "
          "you commit to anything larger."),
    ("p", "There is a second return that clients rarely expect: you find out what your archive "
          "actually contains. The contract everyone refers to that was never signed. The four "
          "versions of a document that differ in one clause. The years where the correspondence "
          "simply stops. That is worth knowing whether or not a machine ever reads it."),
    ("h2", "How it runs"),
    ("p", "A small first contract on your real files, with a fixed scope you name: one property, "
          "one client's matters, one year of correspondence. Acceptance is judged on what it "
          "produces, not on a demonstration. You can stop after any phase and keep everything built "
          "so far."),
    ("p", "The work happens in Europe under a data-processing agreement with Axon Trade ApS, the "
          "Danish company behind Neural Logic. Nothing is read before you have said so in writing, "
          "and only the archives you put in scope are touched."),
    ("h2", "What it is not"),
    ("ul", [
        "<b>Not a system to move into.</b> Your people keep working exactly where they work now.",
        "<b>Not a migration.</b> We work from a copy. Nothing in your systems is changed, moved or "
        "written to.",
        "<b>Not a scanning service.</b> We work from digital copies; paper you already scanned is "
        "read as text like anything else.",
        "<b>Not a promise that AI then works miracles.</b> It is the groundwork that makes the "
        "question worth asking at all.",
    ]),
    ("h2", "Where this stands today"),
    ("p", "Conversion is the part of our work that is furthest along: the same method runs every "
          "day on a catalogue of our own, where a colleague of ours reads a supplier's feed and "
          "keeps a live shop true to it. For document archives, the first client engagement is "
          "being prepared now. We would rather say that plainly than describe a plan in the present "
          "tense."),
]

# ---------------------------------------------------------------------- German

CONVERSION_DE = [
    ("h2", "Die Arbeit, die noch keiner gemacht hat"),
    ("p", "Ein PDF ist ein elektronisches Dokument. Maschinenlesbar ist es deshalb noch lange nicht. "
          "Ein Scan auch nicht, ein Mailverlauf nicht, und ein Ordner namens „final_v3“ erst recht "
          "nicht. Menschen können das alles lesen. Sonst niemand."),
    ("p", "Genau daran scheitern KI-Projekte in Unternehmen mit gewachsenen Archiven. Nicht an den "
          "Modellen. Am Material: Es hat keine Struktur, keine Adressen, und niemand kann sagen, "
          "welche Klausel in welcher Fassung welches Vertrags steht. Was man darauf baut, ist Raterei "
          "mit selbstsicherem Ton."),
    ("h2", "Was Konvertierung wirklich heißt"),
    ("p", "Ihr Archiv wird einmal gelesen, und zwar gründlich. Ein Scan wird zu Text, ein Vertrag zu "
          "Klauseln, ein Mailverlauf zu datierten Nachrichten samt Anhängen, ein Protokoll zu "
          "Beschlüssen. Jedes Stück behält einen Verweis auf die Seite, von der es stammt. So lässt "
          "sich jeder Satz bis zum Original zurückverfolgen."),
    ("p", "Nebenbei entstehen zwei Verzeichnisse: ein Register, das festhält, was in jedem Dokument "
          "steht, und was erwartet wurde und nie gekommen ist; und ein Glossar mit den Begriffen "
          "Ihres Hauses, also den Wörtern, die Ihre Branche und Ihre Leute für die Dinge benutzen."),
    ("h2", "Was Sie bekommen, und behalten"),
    ("ul", [
        "<b>Das konvertierte Archiv</b> in offenen Formaten, nutzbar mit jedem Sprachmodell, mit "
        "unserem oder mit dem, das Sie in drei Jahren wählen.",
        "<b>Das Register:</b> welches Dokument welche Klausel enthält, welches Protokoll "
        "unterschrieben ist, welche Rechnung zu welchem Vorgang gehört, und welche Unterlagen fehlen.",
        "<b>Ihr Glossar:</b> die Begriffe, die bei Ihnen tatsächlich in Gebrauch sind, damit eine "
        "Maschine beim Lesen Ihrer Akten nicht raten muss.",
        "<b>Eine schriftliche Aufstellung dessen, was sich nicht lesen ließ</b>, und warum: "
        "unleserliche Seiten, abgebrochene Scans, leere Dateien. In fast jedem Archiv gibt es ein "
        "paar davon, und niemand weiß es, solange keiner alles gelesen hat.",
    ]),
    ("p", "Alles davon gehört Ihnen und liegt bei Ihnen, nicht in einem System von uns. Das ist "
          "keine Großzügigkeit. Ein Kunde, der nicht gehen kann, ist kein Kunde. Er ist ein "
          "Gefangener."),
    ("h2", "Warum sich das auch für sich allein lohnt"),
    ("p", "Wofür Sie KI am Ende einsetzen und wen Sie damit beauftragen, ist offen. Diese Arbeit "
          "kommt in jedem Fall zuerst. Sie ist der langsame Teil, und sie wird nicht billiger, wenn "
          "man wartet. Einmal erledigt, in einem kleinen Vertrag, mit einem Ergebnis, das Ihnen "
          "gehört, liegt sie hinter Ihnen, bevor Sie sich auf etwas Größeres einlassen."),
    ("p", "Und es gibt einen zweiten Ertrag, mit dem kaum jemand rechnet: Sie erfahren, was in Ihrem "
          "Archiv tatsächlich liegt. Der Vertrag, auf den sich alle berufen und den nie jemand "
          "unterschrieben hat. Die vier Fassungen eines Dokuments, die sich in einer Klausel "
          "unterscheiden. Die Jahre, in denen der Schriftwechsel einfach abreißt. Das ist es wert, "
          "gewusst zu werden, ob nun je eine Maschine mitliest oder nicht."),
    ("h2", "Wie es abläuft"),
    ("p", "Ein kleiner erster Vertrag über Ihre echten Unterlagen, in einem Umfang, den Sie "
          "festlegen: eine Liegenschaft, die Akten eines Mandanten, ein Jahrgang Schriftverkehr. "
          "Abgenommen wird das Ergebnis, nicht eine Vorführung. Nach jeder Phase können Sie aufhören "
          "und behalten alles, was bis dahin entstanden ist."),
    ("p", "Verarbeitet wird in Europa, auf Grundlage eines Auftragsverarbeitungsvertrags mit der "
          "Axon Trade ApS, dem dänischen Unternehmen hinter Neural Logic. Gelesen wird erst, wenn "
          "Sie schriftlich zugestimmt haben, und nur in den Archiven, die Sie dafür freigeben."),
    ("h2", "Was es nicht ist"),
    ("ul", [
        "<b>Kein System, in das Sie umziehen.</b> Ihre Leute arbeiten weiter genau dort, wo sie "
        "heute arbeiten.",
        "<b>Keine Migration.</b> Wir arbeiten mit einer Kopie. In Ihren Systemen wird nichts "
        "geändert, verschoben oder geschrieben.",
        "<b>Kein Scandienst.</b> Wir arbeiten mit digitalen Kopien. Papier, das Sie schon gescannt "
        "haben, wird wie alles andere als Text gelesen.",
        "<b>Kein Versprechen, dass KI danach Wunder wirkt.</b> Es ist die Grundlage, ohne die sich "
        "die Frage gar nicht erst stellt.",
    ]),
    ("h2", "Wo das heute steht"),
    ("p", "Die Konvertierung ist der Teil unserer Arbeit, der am weitesten ist: Dasselbe Verfahren "
          "läuft täglich auf einem Katalog, der uns selbst gehört. Dort liest eine Kollegin von uns "
          "den Feed eines Lieferanten und hält einen laufenden Shop auf dem Stand. Für "
          "Dokumentenarchive bereiten wir gerade die erste Zusammenarbeit mit einem Kunden vor. Das "
          "sagen wir lieber so, wie es ist, als einen Plan im Präsens zu beschreiben."),
]

# ---------------------------------------------------------------------- Danish

CONVERSION_DA = [
    ("h2", "Det arbejde, ingen har gjort endnu"),
    ("p", "En PDF er et elektronisk dokument. Maskinlæsbart er det ikke af den grund. Det er en "
          "scanning heller ikke, og en mailtråd eller en mappe ved navn “endelig_v3” slet ikke. "
          "Mennesker kan læse det hele. Det kan ingen andre."),
    ("p", "Det er lige der, AI-projekter i virksomheder med rigtige arkiver går i stå. Ikke på "
          "modellerne. På materialet: Det har ingen struktur, ingen adresser, og ingen kan sige, "
          "hvilken bestemmelse der står i hvilken version af hvilken kontrakt. Det, man bygger "
          "ovenpå, er gætværk med selvsikker stemme."),
    ("h2", "Hvad konvertering egentlig vil sige"),
    ("p", "Dit arkiv bliver læst én gang, og grundigt. En scanning bliver til tekst, en kontrakt "
          "til bestemmelser, en mailtråd til daterede beskeder med vedhæftninger, et referat til "
          "beslutninger. Hver del beholder en henvisning til den side, den kom fra. Så kan enhver "
          "sætning spores tilbage til originalen."),
    ("p", "Undervejs opstår to fortegnelser: et register over, hvad hvert dokument indeholder, og "
          "hvad der var ventet og aldrig kom; og et glossar med husets egne ord, altså de begreber "
          "jeres fag og jeres folk bruger om tingene."),
    ("h2", "Det, du får, og beholder"),
    ("ul", [
        "<b>Det konverterede arkiv</b> i åbne formater, brugbart med enhver sprogmodel, vores eller "
        "den, du vælger om tre år.",
        "<b>Registeret:</b> hvilket dokument der rummer hvilken bestemmelse, hvilket referat der er "
        "underskrevet, hvilken faktura der hører til hvilken sag, og hvilke dokumenter der mangler.",
        "<b>Dit glossar:</b> de ord, I faktisk bruger, så en maskine ikke skal gætte, når den læser "
        "dine sager.",
        "<b>En skriftlig opgørelse over det, der ikke kunne læses</b>, og hvorfor: ulæselige sider, "
        "afbrudte scanninger, tomme filer. Næsten alle arkiver har nogle stykker, og ingen ved det, "
        "før nogen har læst det hele.",
    ]),
    ("p", "Det hele er dit og ligger hos dig, ikke i et system hos os. Det er ikke gavmildhed. En "
          "kunde, der ikke kan gå, er ikke en kunde. Det er en fange."),
    ("h2", "Hvorfor det kan betale sig helt i sig selv"),
    ("p", "Hvad du ender med at bruge AI til, og hvem du får til at bygge det, er åbent. Det her "
          "arbejde kommer først uanset hvad. Det er den langsomme del, og den bliver ikke billigere "
          "af at vente. Gjort én gang, på en lille kontrakt, med et resultat der er dit, ligger den "
          "bag dig, før du binder dig til noget større."),
    ("p", "Og der er et afkast mere, som de færreste regner med: Du finder ud af, hvad der faktisk "
          "ligger i dit arkiv. Kontrakten, alle henviser til, og som aldrig blev underskrevet. De "
          "fire versioner af et dokument, der adskiller sig på én bestemmelse. Årene, hvor "
          "brevvekslingen bare stopper. Det er værd at vide, uanset om en maskine nogensinde kommer "
          "til at læse med."),
    ("h2", "Sådan foregår det"),
    ("p", "En lille første kontrakt på dine rigtige filer, i et omfang, du selv sætter: én ejendom, "
          "én klients sager, én årgang korrespondance. Det er resultatet, der bliver godkendt, ikke "
          "en demonstration. Efter hver fase kan du stoppe og beholde alt, der er lavet indtil da."),
    ("p", "Behandlingen sker i Europa på grundlag af en databehandleraftale med Axon Trade ApS, det "
          "danske selskab bag Neural Logic. Der læses først, når du har sagt ja på skrift, og kun i "
          "de arkiver, du frigiver."),
    ("h2", "Det, det ikke er"),
    ("ul", [
        "<b>Ikke et system, du skal flytte ind i.</b> Dine folk arbejder videre præcis der, hvor de "
        "arbejder i dag.",
        "<b>Ikke en migrering.</b> Vi arbejder på en kopi. Der bliver hverken ændret, flyttet eller "
        "skrevet noget i dine systemer.",
        "<b>Ikke en scanningsservice.</b> Vi arbejder ud fra digitale kopier. Papir, du allerede har "
        "scannet, bliver læst som tekst ligesom alt andet.",
        "<b>Ikke et løfte om, at AI derefter gør mirakler.</b> Det er grundarbejdet, uden hvilket "
        "spørgsmålet slet ikke kan stilles.",
    ]),
    ("h2", "Hvor det står i dag"),
    ("p", "Konverteringen er den del af vores arbejde, der er nået længst: Den samme metode kører "
          "hver dag på et katalog, vi selv ejer. Der læser en kollega hos os en leverandørs feed og "
          "holder en levende webshop opdateret. For dokumentarkiver er vi ved at forberede det "
          "første kundeforløb nu. Det siger vi hellere, som det er, end at beskrive en plan i nutid."),
]
