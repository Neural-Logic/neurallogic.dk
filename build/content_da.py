"""The four reading pages of neurallogic.dk in Danish (Decision #280, 20 September 2026).

Written under mandate M-018 (Decision #281): from the meaning, as a Danish writer would put
it, never sentence by sentence from the English. The reader is addressed as "du", the way
Danish web copy does. The facts, promises and status lines are the same as on the English
pages (Frida and Vera under preparation, Pia running daily on a shop of our own); the
sentences are not. If the English changes in substance, this changes with it.
"""

HOW_IT_WORKS_DA = [
    ("h2", "Det, du giver os"),
    ("p", "En kopi. Ikke mere. Ingen migrering, intet nyt system, intet års forberedelse. En daglig "
          "kopi af de arkiver, du har i forvejen: datarummet, mailarkivet, bogføringseksporten, "
          "fællesdrevet, og de scanninger, ingen har åbnet, siden de blev lagt væk."),
    ("p", "Der bliver ikke læst noget, før du har sagt ja på skrift. Grundlaget er en "
          "databehandleraftale med Axon Trade ApS, det danske selskab bag Neural Logic. Hvilke "
          "arkiver der er med, bestemmer du. Det er grænsen."),
    ("h2", "Konvertering: Filer bliver til et arkiv med adresser"),
    ("p", "Hvert dokument bliver læst én gang, og grundigt. En scanning bliver til tekst, en "
          "kontrakt til bestemmelser, en mailtråd til daterede beskeder, et referat til beslutninger. "
          "Hver del beholder en henvisning til den side, den kom fra. Så kan enhver sætning spores "
          "tilbage til originalen."),
    ("p", "Resultatet er et arkiv, der er dit: kontrolleret, adresserbart og brugbart med enhver "
          "sprogmodel, vores eller den, du vælger om tre år. Det er ikke en tilfældighed. En kunde, "
          "der ikke kan gå, er ikke en kunde. Det er en fange."),
    ("h2", "Registeret: Det, der er, og det, der mangler"),
    ("p", "Mens der læses, opstår et register. Her står, hvilken kontrakt der rummer hvilken "
          "bestemmelse, hvilket referat der er underskrevet, hvilken faktura der hører til hvilken "
          "sag, og hvilket dokument der var ventet og aldrig kom. Registeret er en optegnelse. Ikke "
          "en hukommelse."),
    ("p", "Derfor er “ikke fundet” et rigtigt svar hos os. Når kollegaen siger, at "
          "opsigelsesbestemmelsen mangler, ved hun det fra registeret: Hun kender hvert dokument, "
          "hun har læst, og hvert sted, bestemmelsen kunne have stået. Det er ikke en model, der "
          "ikke lige kan huske."),
    ("h2", "At læse en sag"),
    ("p", "Du spørger om en sag, en ejendom, en kunde, en kontrakt, et projekt. Kollegaen samler den "
          "komplette sag, kronologisk, på tværs af alle de arkiver, der er med. De steder, hvor "
          "spørgsmålet afgøres, citerer hun ord for ord med henvisning til originalen. Og hun siger "
          "klart, hvad hun ledte efter og ikke fandt."),
    ("p", "Det, du får, er en sag, ikke et chatsvar: dokumenterne, deres rækkefølge, de afgørende "
          "ord, hullerne. At læse og beslutte er et menneskes arbejde."),
    ("h2", "Hvert citat bliver kontrolleret"),
    ("p", "Intet citat når dig, før det er holdt op mod kildedokumentet ord for ord. Passer det "
          "ikke, bliver det holdt tilbage, og du får det at vide. En kollega, der citerer en kontrakt "
          "næsten rigtigt, er værre end ingen kollega. Fejlen ligner nemlig sandheden til "
          "forveksling."),
    ("h2", "To roller, én grænse"),
    ("p", "Kollegaen, der læser dine dokumenter, kører på en europæisk model, Mistral, i Europa og "
          "under en europæisk kontrakt. Ingen dokumenter kommer over den grænse."),
    ("p", "Bag hende står en supervisor, der aldrig får et dokument eller et navn at se. Hun ser "
          "kun, hvordan arbejdet gik: hvilken slags spørgsmål, hvor mange dokumenter, hvilket ord der "
          "manglede, hvor læsningen ramte ved siden af. Fordi intet af dit når frem til hende, kan "
          "hun vælges efter, hvor godt hun tænker, og ikke efter, hvor hun står. I dag er det Claude "
          "fra Anthropic, efter vores mening den bedste model til den slags opgaver. Hun gør kollegaen "
          "lidt bedre hver nat, uden adgang til dine data."),
    ("h2", "Det, det ikke er"),
    ("ul", [
        "<b>Ikke en chatbot på intranettet.</b> Kollegaen svarer ud fra et register, der opstod, "
        "mens dine dokumenter blev læst, ikke ud fra det, en model har husket om dem.",
        "<b>Ikke en beslutningstager.</b> Hun lægger fakta frem. Det er et menneske, der beslutter.",
        "<b>Ikke en dommer over mennesker.</b> Sager om bygninger, produkter, kontrakter, forløb. "
        "Ingen karakterer, ingen ranglister, ingen forudsigelser om personer.",
        "<b>Ikke en, der skriver i dine systemer.</b> Der skrives kun tilbage, hvis du vil have det, "
        "og reglerne tillader det. Som udgangspunkt er det slået fra.",
    ]),
    ("h2", "Hvor det står i dag"),
    ("p", "Frida, dokumentkollegaen, er under forberedelse; det første kundeforløb er vi ved at "
          "forberede nu. Vera, supervisoren, er under forberedelse. Pia, en katalogkollega bygget "
          "efter samme metode, arbejder hver dag i en webshop, vi selv ejer: Hun læser en "
          "leverandørs feed og holder shoppen opdateret hver dag."),
]

QUESTIONS_DA = [
    ("Hvad får vi helt konkret fra Neural Logic?",
     ["En AI-kollega, der læser de arkiver, din virksomhed har i forvejen. Spørger du om en sag, "
      "får du den komplette sag i kronologisk orden: de afgørende steder citeret ord for ord med "
      "henvisning til originalen, og klar besked om, hvad der blev ledt efter og ikke fundet.",
      "Oven i det får du selve arkivet: dine filer i en kontrolleret, adresserbar form, der virker "
      "med enhver sprogmodel, og et register, der holder styr på, hvad hvert dokument indeholder."]),
    ("Forlader vores data Europa?",
     ["Nej. Kollegaen, der læser dine dokumenter, kører på en europæisk model, Mistral, i Europa og "
      "under en europæisk kontrakt. Det juridiske grundlag er en databehandleraftale med Axon Trade "
      "ApS, et dansk selskab.",
      "Supervisoren, der gør kollegaen bedre natten over, ser aldrig et dokument eller et navn. "
      "Derfor kan hun vælges efter sine evner og ikke efter, hvor hun står: I dag er det Claude fra "
      "Anthropic, som kører uden for Europa. Supervisoren ser kun, hvordan arbejdet gik: hvad der blev "
      "spurgt om, hvor mange dokumenter, hvilket ord der manglede. Dit materiale ser hun aldrig."]),
    ("Skal vi flytte vores dokumenter eller skifte system?",
     ["Nej. En daglig kopi af de arkiver, du har i forvejen, er nok: datarum, mailarkiv, "
      "bogføringseksport, fællesdrev. Intet flytter, og dine folk arbejder videre præcis der, hvor "
      "de arbejder i dag."]),
    ("Hvilke arkiver og filer kan kollegaen læse?",
     ["Kontrakter, korrespondance, fakturaer, referater, rapporter og scanninger, fra flere arkiver "
      "på én gang. Scannet papir bliver læst som tekst. Dokumenter, der aldrig har kunnet søges i, "
      "hører dermed til sagen som alle andre."]),
    ("Hvad sker der, hvis svaret slet ikke står i dokumenterne?",
     ["Så får du netop det at vide. “Ikke fundet” er et fuldgyldigt svar hos os, og det kommer fra "
      "registeret, der opstod, mens alle dokumenterne blev læst, ikke fra en models hukommelse. Om "
      "en bestemmelse, en underskrift eller et referat mangler, er en kendsgerning om dit arkiv. Og "
      "sådan bliver det besvaret.",
      "I det arbejde, vores kunder går op i, er visheden om, at noget mangler, som regel lige så "
      "meget værd som fundet."]),
    ("Hvordan forhindrer I opdigtede citater?",
     ["Hvert citat bliver holdt op mod kildedokumentet ord for ord, før det når læseren. Passer det "
      "ikke, bliver det holdt tilbage, og læseren får det at vide. Hos os slipper intet igennem, bare "
      "fordi det lyder rigtigt."]),
    ("Hvad er forskellen på det og ChatGPT eller Copilot på vores filer?",
     ["En almindelig assistent svarer ud fra det, den har fundet, og det, den kan huske. Det, den "
      "ikke fandt, kan den ikke fortælle dig om. I en sag, hvor der står penge eller ansvar på spil, "
      "er det lige præcis den forskel, der betyder noget.",
      "En dokumentkollega læser hvert dokument, der hører med, fører et register over det, citerer "
      "kun det, hun har kontrolleret mod kilden, og nævner hullerne. Og hun holder grænsen: Dine "
      "dokumenter bliver inden for en europæisk kontrakt."]),
    ("Hvem skriver vi kontrakt med, og hvem hæfter?",
     ["Axon Trade ApS, et dansk anpartsselskab med hjemsted i København, CVR 45 92 07 63. Neural "
      "Logic er et brand under det selskab, ikke et selskab i sig selv. Kontrakter, fakturaer og "
      "databehandleraftalen står alle i Axon Trade ApS' navn, tegnet af selskabets direktør."]),
    ("Hvordan ser et første forløb ud?",
     ["Lille og målbart. En kort første kontrakt på en rigtig sag hos jer, ingen demonstration. Det, "
      "der kommer ud af det, er det, der bliver taget stilling til. Derefter følger to korte faser "
      "mere. Efter hver fase kan du stoppe og beholde alt, der er lavet indtil da: det konverterede "
      "arkiv, registeret, glossaret.",
      "Meningen er, at du beslutter ud fra beviser i dine egne sager, ikke ud fra slides. Og den "
      "første fase kan betale sig, selv hvis du stopper der. Hvorfor, står i næste svar."]),
    ("Og hvis vi stopper efter første fase, hvad står vi så med?",
     ["Det, enhver virksomhed før eller siden får brug for alligevel: dine filer i et kontrolleret, "
      "maskinlæsbart arkiv, plus et register over, hvad hvert dokument indeholder, og et glossar med "
      "de ord, I bruger i huset. Intet af det er skåret til vores software. Det virker med enhver "
      "sprogmodel, vores eller den, du vælger om tre år.",
      "Det arbejde slipper næsten ingen virksomhed for. Dokumenter, der kun findes som scanninger, "
      "PDF'er og mailtråde, kan ingen AI bruge, som man bør stole på. Konverteringen er den langsomme "
      "del, ikke den kloge, der kommer bagefter. At få den gjort på en lille første kontrakt, på "
      "rigtige sager, med et resultat der er dit, er den billige måde at få den overstået på.",
      "Derfor er første fase hos os et løfte, ikke en prøve. Uanset hvad du beslutter bagefter, er "
      "du længere fremme, end du var."]),
    ("Hvad koster det?",
     ["Prisen afhænger af forløbet, for arbejdet afhænger af, hvor meget du har, og i hvilken stand. "
      "Første fase holder vi bevidst lille, så den første beslutning også er lille. Skriv til os "
      "med en fornemmelse af, hvilke arkiver det drejer sig om, så får du et klart svar."]),
    ("Hvilke sprog arbejder kollegaen på?",
     ["Dansk, tysk og engelsk. Selskabet ligger i København, og stifteren er tysk. Der skrives "
      "direkte på alle tre sprog, uden oversættelse imellem."]),
    ("Hvem står bag Neural Logic?",
     ["Thomas Möller, stifter og eneejer af Axon Trade ApS i København. Selskabet driver også "
      "hockeybutikken Hockey24. Selskabsoplysningerne, inklusive udskriften fra Erhvervsstyrelsen, "
      "finder du på <a href=\"https://axontrade.dk/\">Axon Trades side</a>."]),
]

PROPERTY_DA = [
    ("h2", "Problemet i branchen"),
    ("p", "Til en ejendom hører årtiers papir: købet, lejekontrakterne med tillæg, "
          "overdragelsesprotokollerne, mangellisterne, brevvekslingen med lejere og håndværkere, "
          "forsikringssagen, ingen fik lukket, og fakturaerne til en reparation, som alle husker "
          "forskelligt. Det hele ligger i datarummet, i mailarkivet og på fællesdrevet. Og ingen har "
          "tid til at læse alle tre."),
    ("p", "Så spørgsmålet “Hvad var det egentlig, vi aftalte om det tag, og hvornår?” koster en "
          "eftermiddag. Og oftere, end nogen vil indrømme, bliver det besvaret efter hukommelsen."),
    ("h2", "Det, kollegaen gør ved det"),
    ("ul", [
        "<b>Den komplette sag om ét objekt.</b> Alt om en ejendom, et lejemål eller et lejeforhold, "
        "kronologisk, fra alle de arkiver, der er med.",
        "<b>Den afgørende bestemmelse, ordret.</b> Hvilken version af lejekontrakten der gælder, og "
        "hvad den siger om den forpligtelse, det handler om, ord for ord, med henvisning til siden.",
        "<b>Det, der mangler, ved navn.</b> Overdragelsesprotokollen, der aldrig blev underskrevet. "
        "Tillægget, alle henviser til, og som ikke ligger nogen steder. Attesten, der er udløbet. "
        "Fra registeret, ikke fra et gæt.",
        "<b>Historien i en tvist.</b> Hver besked, hvert referat, hver faktura i et forløb, samlet, "
        "før en advokat får penge for at gøre det.",
    ]),
    ("h2", "Det, den ikke gør"),
    ("p", "Den siger ikke noget om personer: ingen vurdering af lejere, ingen spådom om, hvem der "
          "betaler. Kun sager om bygninger, kontrakter og forløb. Den skriver ikke tilbage i dit "
          "administrationssystem, medmindre du vil have det, og reglerne tillader det. Og den "
          "beslutter ingenting. Sagen læses af et menneske, og det er mennesket, der handler."),
    ("h2", "Sådan kunne det begynde hos jer"),
    ("p", "Med én rigtig ejendom eller én rigtig tvist fra jeres eget arkiv, under en "
          "databehandleraftale. Bedøm resultatet på en sag, hvor du kender svaret. Mere ærligt kan "
          "man ikke prøve sådan en kollega af."),
    ("p", "Efter første fase ligger dine sager som et kontrolleret, maskinlæsbart arkiv. Det er dit, "
          "uanset hvad du beslutter bagefter. Ejendomsporteføljer er lige præcis den slags papir, der "
          "før eller siden skal konverteres. At få det gjort på en lille kontrakt, på rigtige sager, "
          "er den billigste måde at få det overstået på."),
    ("p", "Frida, dokumentkollegaen, er under forberedelse; det første kundeforløb er vi ved at "
          "forberede nu. Den, der skriver nu, er med til at bestemme, hvilke sager hun arbejder på "
          "først."),
]

LAW_DA = [
    ("h2", "Problemet i branchen"),
    ("p", "Sagen er arbejdet. En sag kommer med årevis af korrespondance, udkast, der ligner "
          "hinanden til forveksling, et aftalebrev et sted i mappen, fakturaer på enkelte faser og en "
          "klient, der husker et tilsagn, som måske står på skrift, og måske ikke. At læse det hele "
          "kan kun faktureres i teorien. I praksis sker det sidst på dagen, hos den, der dårligst har "
          "råd til det."),
    ("h2", "Det, kollegaen gør ved det"),
    ("ul", [
        "<b>Hele sagen, i rækkefølge.</b> Hvert dokument og hver besked i en sag, dateret, fra alle "
        "de arkiver, sagen rører ved.",
        "<b>Den gældende ordlyd, citeret.</b> Hvilken version af en bestemmelse der gælder, og hvad "
        "den faktisk siger, kontrolleret ord for ord mod kilden, før du får det at se.",
        "<b>Huller som huller.</b> Intet underskrevet aftalebrev, ingen skriftlig bekræftelse af det "
        "mundtlige tilsagn, et bilag, der mangler: nævnt ud fra registeret over det, der blev læst.",
        "<b>Et spor, der holder.</b> Hvert udsagn bærer en henvisning til originalen. Ræsonnementet "
        "kan efterprøves af en, der ikke var med.",
    ]),
    ("h2", "Fortrolighed og grænsen"),
    ("p", "Behandlingen sker i Europa på grundlag af en databehandleraftale med Axon Trade ApS. "
          "Supervisoren, der gør kollegaen bedre natten over, ser hverken dokumenter eller navne. "
          "Der læses kun i de arkiver, du frigiver, og først når du har sagt ja på skrift."),
    ("p", "Kollegaen dømmer ikke mennesker og rådgiver ikke. Hun lægger frem, hvad der står i "
          "dokumenterne, og hvad der ikke gør. Den faglige vurdering bliver, hvor den hører hjemme. "
          "Det gør ansvaret også."),
    ("h2", "Sådan kunne det begynde hos jer"),
    ("p", "Med én afsluttet sag, du kender ud og ind, læst fra jeres eget arkiv. Så kan du holde "
          "resultatet op mod det, du ved i forvejen. En lille første kontrakt; det konverterede arkiv "
          "beholder du under alle omstændigheder. Det er den kontrollerede, maskinlæsbare form af "
          "dine egne sager, som enhver AI de kommende år får brug for alligevel, og som ingen i "
          "sidste ende slipper for at bygge."),
    ("p", "Frida er under forberedelse; det første kundeforløb er vi ved at forberede nu."),
]
