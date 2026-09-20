"""The archive-conversion page, in English, German and Danish.

Lead's ruling of 20 September 2026: the conversion of a company's archive into a
machine-readable form is sold as a thing of its own, because the monthly findability
check found that search returns only tools for it and no company that does the work on
real files. German and Danish get their own page because the German search returns no
vendor of our kind at all, and Denmark is our home market. This narrows, knowingly, the
ruling of 4 September that the site stays English: it applies to this page only.

The three versions must say the same things. If one changes, change all three.
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
    ("h2", "Die Arbeit, die noch niemand gemacht hat"),
    ("p", "Ein PDF ist ein elektronisches Dokument, aber kein maschinenlesbares. Ein Scan ebenso "
          "wenig, ein Mailverlauf auch nicht, und ein Ordner namens „final_v3“ erst recht nicht. "
          "Menschen können das lesen. Alles andere nicht."),
    ("p", "Genau daran scheitern KI-Vorhaben in Unternehmen mit gewachsenen Archiven. An den "
          "Modellen liegt es nicht. Es liegt am Material: keine Struktur, keine Adressen, keine "
          "Möglichkeit zu sagen, welche Klausel in welcher Fassung welches Vertrags steht. Was "
          "darauf aufbaut, ist Raten in selbstsicherem Ton."),
    ("h2", "Was Konvertierung wirklich bedeutet"),
    ("p", "Ihr Archiv wird einmal gelesen, und zwar richtig. Aus einem Scan wird Text. Aus einem "
          "Vertrag werden Klauseln. Aus einem Mailverlauf werden datierte Nachrichten mit ihren "
          "Anhängen. Aus einem Protokoll werden Beschlüsse. Jedes Stück behält den Verweis auf die "
          "Seite, aus der es stammt, sodass sich jeder Satz bis zum Original zurückverfolgen lässt."),
    ("p", "Dabei entstehen zwei Verzeichnisse: ein Register dessen, was in jedem Dokument steht — "
          "und was erwartet wurde und nie eingegangen ist — sowie ein Glossar Ihrer eigenen "
          "Begriffe, also der Wörter, die Ihre Branche und Ihr Haus für die Dinge verwenden."),
    ("h2", "Was Sie bekommen und behalten"),
    ("ul", [
        "<b>Das konvertierte Archiv</b> in offenen Formaten, nutzbar mit jedem Sprachmodell — mit "
        "unserem oder mit dem, für das Sie sich in drei Jahren entscheiden.",
        "<b>Das Register:</b> welches Dokument welche Klausel enthält, welches Protokoll "
        "unterschrieben ist, welche Rechnung zu welchem Vorgang gehört und welche Unterlagen fehlen.",
        "<b>Ihr Glossar:</b> die Begriffe, die in Ihrem Haus tatsächlich verwendet werden, damit "
        "eine Maschine beim Lesen Ihrer Akten nicht raten muss.",
        "<b>Eine schriftliche Aufstellung dessen, was nicht gelesen werden konnte</b>, und warum: "
        "unlesbare Seiten, abgebrochene Scans, leere Dateien. In fast jedem Archiv gibt es davon "
        "einige, und niemand weiß es, bevor jemand alles gelesen hat.",
    ]),
    ("p", "Alles davon gehört Ihnen und liegt bei Ihnen, nicht eingeschlossen in einem System von "
          "uns. Das ist keine Großzügigkeit: Ein Kunde, der nicht gehen kann, ist kein Kunde, "
          "sondern ein Gefangener."),
    ("h2", "Warum sich das für sich allein lohnt"),
    ("p", "Wofür Sie KI am Ende auch einsetzen und wen Sie damit auch beauftragen: Diese Arbeit "
          "steht davor. Sie ist der langsame Teil, und sie wird durch Warten nicht billiger. Einmal "
          "erledigt, in einem kleinen Vertrag, mit einem Ergebnis, das Ihnen gehört, liegt sie "
          "hinter Ihnen, bevor Sie sich auf etwas Größeres festlegen."),
    ("p", "Dazu kommt ein zweiter Ertrag, mit dem kaum jemand rechnet: Sie erfahren, was in Ihrem "
          "Archiv tatsächlich liegt. Der Vertrag, auf den sich alle berufen und den nie jemand "
          "unterschrieben hat. Die vier Fassungen eines Dokuments, die sich in einer Klausel "
          "unterscheiden. Die Jahre, in denen der Schriftwechsel einfach abbricht. Das ist es wert, "
          "gewusst zu werden, ganz gleich ob je eine Maschine mitliest."),
    ("h2", "Wie es abläuft"),
    ("p", "Ein kleiner erster Vertrag über Ihre echten Unterlagen, mit einem Umfang, den Sie "
          "festlegen: eine Liegenschaft, die Akten eines Mandanten, ein Jahrgang Schriftverkehr. "
          "Abgenommen wird, was dabei herauskommt, nicht eine Vorführung. Sie können nach jeder "
          "Phase aufhören und behalten alles, was bis dahin entstanden ist."),
    ("p", "Die Verarbeitung findet in Europa statt, unter einem Auftragsverarbeitungsvertrag mit der "
          "Axon Trade ApS, dem dänischen Unternehmen hinter Neural Logic. Gelesen wird nichts, bevor "
          "Sie schriftlich zugestimmt haben, und nur in den Archiven, die Sie dafür benennen."),
    ("h2", "Was es nicht ist"),
    ("ul", [
        "<b>Kein System, in das Sie umziehen.</b> Ihre Leute arbeiten weiter genau dort, wo sie "
        "heute arbeiten.",
        "<b>Keine Migration.</b> Wir arbeiten mit einer Kopie. In Ihren Systemen wird nichts "
        "geändert, verschoben oder geschrieben.",
        "<b>Kein Scandienst.</b> Wir arbeiten mit digitalen Kopien; bereits gescanntes Papier wird "
        "wie alles andere als Text gelesen.",
        "<b>Kein Versprechen, dass KI danach Wunder wirkt.</b> Es ist die Grundlage, die die Frage "
        "überhaupt erst sinnvoll macht.",
    ]),
    ("h2", "Wo das heute steht"),
    ("p", "Die Konvertierung ist der am weitesten gediehene Teil unserer Arbeit: Dasselbe Verfahren "
          "läuft täglich auf einem Katalog von uns selbst, wo eine Kollegin von uns den Feed eines "
          "Lieferanten liest und einen laufenden Shop danach richtig hält. Für Dokumentenarchive "
          "wird gerade die erste Zusammenarbeit mit einem Kunden vorbereitet. Das sagen wir lieber "
          "klar, als einen Plan im Präsens zu beschreiben."),
]

# ---------------------------------------------------------------------- Danish

CONVERSION_DA = [
    ("h2", "Arbejdet, som ingen har lavet endnu"),
    ("p", "En PDF er et elektronisk dokument, men ikke et maskinlæsbart. Det samme gælder et scan, "
          "en mailtråd og en mappe, der hedder “endelig_v3”. Mennesker kan læse det. Alt andet kan "
          "ikke."),
    ("p", "Det er dér, AI-projekter i virksomheder med rigtige arkiver går i stå. Modellerne fejler "
          "ikke noget. Materialet gør: ingen struktur, ingen adresser, ingen måde at sige hvilken "
          "bestemmelse der står i hvilken version af hvilken kontrakt. Det, der bygges ovenpå, er "
          "gætteri i en selvsikker tone."),
    ("h2", "Hvad konvertering faktisk er"),
    ("p", "Jeres arkiv bliver læst én gang, ordentligt. Et scan bliver til tekst. En kontrakt bliver "
          "til bestemmelser. En mailtråd bliver til daterede beskeder med deres vedhæftninger. Et "
          "referat bliver til beslutninger. Hver del beholder et link tilbage til den side, den kom "
          "fra, så enhver sætning kan spores til originalen."),
    ("p", "Undervejs bliver to ting skrevet ned: et register over, hvad hvert dokument indeholder — "
          "og hvad der var ventet og aldrig kom — og et glossar over jeres egne ord, altså de "
          "begreber jeres fag og jeres hus bruger om tingene."),
    ("h2", "Hvad I får, og beholder"),
    ("ul", [
        "<b>Det konverterede arkiv</b> i åbne formater, som kan bruges af enhver sprogmodel — vores "
        "eller den, I vælger om tre år.",
        "<b>Registeret:</b> hvilket dokument der indeholder hvilken bestemmelse, hvilket referat der "
        "er underskrevet, hvilken faktura der hører til hvilken sag, og hvilke dokumenter der "
        "mangler.",
        "<b>Jeres glossar:</b> de begreber, I rent faktisk bruger, så en maskine ikke skal gætte sig "
        "frem, når den læser jeres sager.",
        "<b>En skriftlig opgørelse over, hvad der ikke kunne læses</b>, og hvorfor: ulæselige sider, "
        "afbrudte scan, tomme filer. Næsten alle arkiver rummer nogle stykker, og ingen ved det, før "
        "nogen har læst det hele.",
    ]),
    ("p", "Det hele er jeres og ligger hos jer, ikke låst inde i et system hos os. Det er ikke "
          "gavmildhed: en kunde, der ikke kan gå, er ikke en kunde, men en fange."),
    ("h2", "Hvorfor det kan betale sig i sig selv"),
    ("p", "Uanset hvad I til sidst bruger AI til, og uanset hvem I hyrer til at bygge det, kommer "
          "dette arbejde først. Det er den langsomme del, og det bliver ikke billigere af at vente. "
          "Gjort én gang, på en lille kontrakt, med et resultat der er jeres, ligger det bag jer, "
          "før I binder jer til noget større."),
    ("p", "Der er et afkast mere, som de færreste regner med: I finder ud af, hvad jeres arkiv "
          "faktisk indeholder. Kontrakten, alle henviser til, og som aldrig blev underskrevet. De "
          "fire versioner af et dokument, der adskiller sig på én bestemmelse. Årene, hvor "
          "korrespondancen bare holder op. Det er værd at vide, uanset om en maskine nogensinde "
          "læser med."),
    ("h2", "Sådan foregår det"),
    ("p", "En lille første kontrakt på jeres rigtige filer, med et omfang, I selv sætter: én "
          "ejendom, én klients sager, én årgang korrespondance. Der bliver taget stilling til det, "
          "der kommer ud af det, ikke til en demonstration. I kan stoppe efter enhver fase og "
          "beholde alt, hvad der er bygget indtil da."),
    ("p", "Arbejdet foregår i Europa under en databehandleraftale med Axon Trade ApS, det danske "
          "selskab bag Neural Logic. Intet bliver læst, før I har sagt ja skriftligt, og kun i de "
          "arkiver, I peger på."),
    ("h2", "Hvad det ikke er"),
    ("ul", [
        "<b>Ikke et system, I skal flytte ind i.</b> Jeres folk arbejder videre præcis, hvor de "
        "arbejder i dag.",
        "<b>Ikke en migrering.</b> Vi arbejder på en kopi. Intet i jeres systemer bliver ændret, "
        "flyttet eller skrevet til.",
        "<b>Ikke en scanningsservice.</b> Vi arbejder ud fra digitale kopier; papir, I allerede har "
        "scannet, bliver læst som tekst ligesom alt andet.",
        "<b>Ikke et løfte om, at AI derefter gør mirakler.</b> Det er grundarbejdet, der gør "
        "spørgsmålet værd at stille.",
    ]),
    ("h2", "Hvor det står i dag"),
    ("p", "Konverteringen er den del af vores arbejde, der er nået længst: den samme metode kører "
          "hver dag på et katalog, vi selv ejer, hvor en kollega hos os læser en leverandørs feed og "
          "holder en levende webshop tro mod den. For dokumentarkiver er det første kundeforløb ved "
          "at blive forberedt nu. Det siger vi hellere ligeud end at beskrive en plan i nutid."),
]
