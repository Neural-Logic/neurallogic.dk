"""The four reading pages of neurallogic.dk in Danish (Decision #280, 20 September 2026).

Written to say exactly what the English says, in the register the English uses. If the
English changes, this changes with it: same sections, same claims, same status lines
(Frida and Vera under preparation, Pia running daily on a shop of our own).
"""

HOW_IT_WORKS_DA = [
    ("h2", "Hvad I giver os"),
    ("p", "En kopi. Ikke en migrering, ikke et nyt system at flytte ind i, ikke et års "
          "forberedelse. En daglig kopi af de arkiver, I allerede har: datarummet, mailarkivet, "
          "bogføringseksporten, fællesdrevet, de scan ingen har åbnet, siden de blev arkiveret."),
    ("p", "Intet læses, før I har sagt det skriftligt, i en databehandleraftale med Axon Trade "
          "ApS, det danske selskab bag Neural Logic. I siger, hvilke arkiver der er med, og det er "
          "grænsen."),
    ("h2", "Konvertering: filer bliver til et adresserbart arkiv"),
    ("p", "Hvert dokument læses én gang, ordentligt. Et scan bliver til tekst, en kontrakt bliver "
          "til bestemmelser, en mailtråd bliver til daterede beskeder, et referat bliver til "
          "beslutninger. Hver del beholder et link tilbage til den side, den kom fra, så enhver "
          "sætning kan spores til originalen."),
    ("p", "Resultatet er et arkiv, I ejer: kontrolleret, adresserbart og brugbart med enhver "
          "sprogmodel, vores eller den, I vælger om tre år. Det er med vilje. En kunde, der ikke "
          "kan gå, er ikke en kunde, men en fange."),
    ("h2", "Registeret: hvad der er, og hvad der ikke er"),
    ("p", "Mens dokumenterne læses, bygges et register: hvilken kontrakt der rummer hvilken "
          "bestemmelse, hvilket referat der er underskrevet, hvilken faktura der hører til hvilken "
          "sag, hvilket dokument der var ventet og aldrig kom. Registeret er en optegnelse, ikke en "
          "hukommelse."),
    ("p", "Det er det, der gør “ikke fundet” til et rigtigt svar. Når kollegaen siger, at en "
          "opsigelsesbestemmelse mangler, kommer det fra registeret, som kender hvert dokument, "
          "det har læst, og hvert sted, bestemmelsen kunne have stået. Det er ikke en model, der "
          "ikke kan huske noget."),
    ("h2", "At læse en sag"),
    ("p", "I spørger om en sag, en ejendom, en klient, en kontrakt eller et projekt. Kollegaen "
          "samler den komplette sag i datorækkefølge på tværs af alle arkiver, der er med, citerer "
          "de passager, der afgør spørgsmålet, ord for ord med link til originalen, og siger "
          "ligeud, hvad den ledte efter og ikke fandt."),
    ("p", "Det, der kommer tilbage, er en sag, ikke et chatsvar: dokumenterne, den rækkefølge de "
          "skete i, de afgørende ord og hullerne. Et menneske læser den og beslutter."),
    ("h2", "Hvert citat kontrolleres"),
    ("p", "Før et citat når jer, sammenlignes det ord for ord med kildedokumentet. Stemmer det "
          "ikke, holdes det tilbage, og I får det at vide. En kollega, der citerer en kontrakt "
          "næsten rigtigt, er værre end ingen kollega, fordi fejlen ser præcis ud som sandheden."),
    ("h2", "To roller, én grænse"),
    ("p", "Kollegaen, der læser jeres dokumenter, kører på en europæisk model, Mistral, behandlet "
          "i Europa under en europæisk kontrakt. Dokumenter forlader ikke den grænse."),
    ("p", "Bag hende står en supervisor, der aldrig ser et dokument eller et navn. Den læser kun "
          "arbejdets form: hvilken slags spørgsmål der blev stillet, hvor mange dokumenter der blev "
          "læst, hvilket ord der manglede, hvor læsningen gik galt. Fordi intet af jeres når den, "
          "vælges den efter tænkning frem for placering: i dag er det Claude fra Anthropic, som "
          "kører uden for Europa. Den forbedrer kollegaen natten over, og grænsen holder."),
    ("p", "Vi nævner den ved navn i stedet for at skrive “den stærkeste tilgængelige model”, "
          "fordi en grænse, man ikke kan se, ikke er en grænse, man kan kontrollere. Jeres "
          "dokumenter bliver hos den europæiske model. Supervisoren ser, hvordan arbejdet gik, "
          "aldrig hvad det handlede om."),
    ("h2", "Hvad det ikke er"),
    ("ul", [
        "<b>Ikke en chatbot på jeres intranet.</b> Den svarer fra et kontrolleret register, bygget "
        "mens jeres dokumenter blev læst, ikke fra en models erindring om dem.",
        "<b>Ikke en beslutningstager.</b> Den lægger fakta frem. Et menneske vejer dem og handler.",
        "<b>Ikke en dommer over mennesker.</b> Sager om bygninger, produkter, kontrakter og forløb. "
        "Ingen scorer, ingen ranglister, ingen forudsigelser om personer.",
        "<b>Ikke en skriver i jeres systemer.</b> Tilbageskrivning er som udgangspunkt slået fra "
        "og slås kun til på opfordring, hvor I beder om det, og reglerne tillader det.",
    ]),
    ("h2", "Hvor det står i dag"),
    ("p", "Frida, dokumentkollegaen, er under forberedelse, og det første kundeforløb er ved at "
          "blive forberedt nu. Vera, supervisoren, er under forberedelse. Pia, en katalogkollega "
          "bygget på samme metode, kører hver dag på en webshop, vi selv ejer, læser en "
          "leverandørs feed og holder shoppen tro mod den. Det siger vi hellere ligeud end at "
          "beskrive planer i nutid."),
]

QUESTIONS_DA = [
    ("Hvad leverer Neural Logic egentlig?",
     ["En AI-kollega, der læser de arkiver, jeres virksomhed allerede har, og som for enhver sag, "
      "I spørger om, lægger den komplette sag op i datorækkefølge, citerer de afgørende passager "
      "ord for ord med link til originalen og siger, hvad den ledte efter og ikke fandt.",
      "Ved siden af får I selve arkivet: jeres filer konverteret til en kontrolleret, adresserbar "
      "form, der virker med enhver sprogmodel, og et register over, hvad hvert dokument "
      "indeholder."]),
    ("Forlader vores data Europa?",
     ["Nej. Kollegaen, der læser dokumenter, kører på en europæisk model, Mistral, behandlet i "
      "Europa under en europæisk kontrakt, og arbejdet foregår under en databehandleraftale med "
      "Axon Trade ApS, et dansk selskab.",
      "Supervisoren, der forbedrer kollegaen natten over, ser aldrig et dokument eller et navn, "
      "og vælges derfor efter tænkning frem for placering: i dag er det Claude fra Anthropic, som "
      "kører uden for Europa. Det siger vi ligeud i stedet for at skrive “den stærkeste "
      "tilgængelige model”, fordi en grænse, ingen kan se, ikke er en grænse, nogen kan "
      "kontrollere. Den læser kun arbejdets form — hvad der blev spurgt om, hvor mange dokumenter, "
      "hvilket ord der manglede — og aldrig jeres materiale."]),
    ("Skal vi migrere vores dokumenter eller skifte system?",
     ["Nej. En daglig kopi af de arkiver, I allerede har, er nok: et datarum, et mailarkiv, en "
      "bogføringseksport, et fællesdrev. Intet skal flyttes ind i et nyt system, og jeres folk "
      "arbejder videre præcis, hvor de arbejder i dag."]),
    ("Hvilke slags arkiver og filer kan den læse?",
     ["Kontrakter, korrespondance, fakturaer, referater, rapporter og scan, på tværs af flere "
      "arkiver på én gang. Scannet papir læses som tekst, så dokumenter, der aldrig har været "
      "søgbare, bliver en del af sagen som alle andre."]),
    ("Hvad sker der, når svaret ikke står i dokumenterne?",
     ["I får det at vide. “Ikke fundet” er et fuldgyldigt svar her, og det kommer fra registeret, "
      "der blev bygget, mens hvert dokument blev læst, ikke fra en models hukommelse. Om en "
      "bestemmelse, en underskrift eller et referat mangler, er en kendsgerning om jeres arkiv, "
      "og den besvares som én.",
      "For det meste af det arbejde, vores kunder går op i, er det lige så meget værd at vide, at "
      "noget mangler, som at finde det."]),
    ("Hvordan forhindrer I, at den opfinder citater?",
     ["Hvert citat sammenlignes ord for ord med sit kildedokument, før det når læseren. Stemmer "
      "det ikke, holdes det tilbage, og læseren får det at vide. Intet når jer, bare fordi det "
      "lyder rigtigt."]),
    ("Hvordan adskiller det sig fra at spørge ChatGPT eller Copilot om vores filer?",
     ["En almindelig assistent svarer ud fra det, den fandt, og det, den husker, og den kan ikke "
      "fortælle jer, hvad den ikke fandt. Det er den forskel, der betyder noget i en sag, der "
      "bærer penge eller ansvar.",
      "En dokumentkollega læser hvert dokument, der er med, fører et register over, hvad de "
      "indeholder, citerer kun det, den har kontrolleret mod kilden, og nævner hullerne. Den "
      "holder også grænsen: jeres dokumenter bliver inden for en europæisk kontrakt."]),
    ("Hvem skriver vi kontrakt med, og hvem hæfter?",
     ["Axon Trade ApS, et dansk anpartsselskab i København, CVR 45 92 07 63. Neural Logic er et "
      "brand under det selskab, ikke en selvstændig juridisk enhed. Kontrakter, fakturaer og "
      "databehandleraftalen nævner alle Axon Trade ApS, og selskabet tegnes af sin direktør."]),
    ("Hvordan ser et første forløb ud?",
     ["Lille og målbart. En kort første kontrakt på en rigtig sag hos jer frem for en "
      "demonstration, hvor der tages stilling til det, den leverer; derefter to yderligere korte "
      "faser. I kan stoppe efter enhver fase og beholde alt, der er bygget indtil da, inklusive det "
      "konverterede arkiv, registeret og glossaret.",
      "Meningen med at begynde sådan er, at I beslutter på beviser fra jeres egne filer, ikke på "
      "slides. Og den første fase er værd at have, selv hvis I vælger at stoppe der, af den grund, "
      "der står i næste svar."]),
    ("Hvis vi stopper efter den første fase, hvad har vi så egentlig fået?",
     ["Det, enhver virksomhed alligevel får brug for: jeres filer konverteret til et kontrolleret, "
      "maskinlæsbart arkiv, med et register over, hvad hvert dokument indeholder, og et glossar over "
      "jeres egne ord. Det er ikke bygget til vores software. Det virker med enhver sprogmodel, "
      "vores eller den, I vælger om tre år.",
      "Næsten alle virksomheder skal på et tidspunkt have gjort dette arbejde. Dokumenter, der kun "
      "findes som scan, PDF'er og mailtråde, kan ikke bruges af nogen AI, der er værd at stole på, "
      "og at konvertere dem er den langsomme del — ikke den kloge del, der kommer bagefter. At gøre "
      "det på en lille første kontrakt, på rigtige sager, med et resultat der er jeres, er en "
      "billig måde at få det overstået på.",
      "Derfor behandler vi den første fase som et løfte og ikke som en prøve: uanset hvad I "
      "beslutter om os bagefter, er I længere fremme, end I var."]),
    ("Hvad koster det?",
     ["Det prissættes pr. forløb, fordi arbejdet afhænger af, hvor meget I har, og i hvilken "
      "stand. Den første fase er bevidst lille, så den første beslutning også er lille. Skriv til "
      "os med en grov idé om de arkiver, det drejer sig om, så får I et klart svar."]),
    ("Hvilke sprog arbejder kollegaen på?",
     ["Dansk, tysk og engelsk. Selskabet ligger i København, og stifteren er tysk, så det "
      "skriftlige arbejde foregår på alle tre sprog uden oversættelse imellem."]),
    ("Hvem står bag Neural Logic?",
     ["Thomas Möller, stifter og eneejer af Axon Trade ApS i København, som også driver "
      "hockeybutikken Hockey24. Selskabets oplysninger, inklusive udskriften fra "
      "Erhvervsstyrelsen, står på <a href=\"https://axontrade.dk/\">Axon Trades side</a>."]),
]

PROPERTY_DA = [
    ("h2", "Problemet i denne branche"),
    ("p", "En ejendom bærer årtiers papir: købet, lejekontrakterne og deres tillæg, "
          "overdragelsesprotokollerne, mangellisterne, korrespondancen med lejere og håndværkere, "
          "forsikringssagen, ingen fik lukket, fakturaerne, der hører til en reparation, nogen "
          "husker anderledes. Det ligger i et datarum, et mailarkiv og på et fællesdrev, og ingen "
          "har tid til at læse alle tre."),
    ("p", "Så spørgsmålet “hvad aftalte vi egentlig om det tag, og hvornår” koster en eftermiddag "
          "og besvares oftere efter hukommelsen, end nogen indrømmer."),
    ("h2", "Hvad kollegaen gør med det"),
    ("ul", [
        "<b>Den komplette sag for ét objekt.</b> Alt om en ejendom, et lejemål eller et "
        "lejeforhold, i datorækkefølge, på tværs af alle arkiver, der er med.",
        "<b>Den bestemmelse, der afgør det, citeret.</b> Hvilken version af lejekontrakten der "
        "gælder, hvad den siger om den pågældende forpligtelse, ord for ord, med link til den side, "
        "det kom fra.",
        "<b>Det, der mangler, nævnt.</b> Overdragelsesprotokollen, der aldrig blev underskrevet, "
        "tillægget, der henvises til, men ikke findes, attesten, der udløb. Fra registeret, ikke fra "
        "et gæt.",
        "<b>Historien i en tvist.</b> Hver besked, hvert referat og hver faktura, der rører en sag, "
        "samlet, før en advokat får betaling for at samle den.",
    ]),
    ("h2", "Hvad den ikke gør"),
    ("p", "Den fremsætter ingen udsagn om personer: ingen scorer på lejere, ingen forudsigelser om, "
          "hvem der betaler. Kun sager om bygninger, kontrakter og forløb. Den skriver intet tilbage "
          "i jeres administrationssystem, medmindre I beder om det, og reglerne tillader det. Og "
          "den beslutter intet; et menneske læser sagen og handler."),
    ("h2", "Sådan ville det begynde hos jer"),
    ("p", "Med ét rigtigt objekt eller én rigtig tvist fra jeres eget arkiv, under en "
          "databehandleraftale. I bedømmer resultatet på en sag, hvis svar I allerede kender, for "
          "det er den eneste ærlige måde at afprøve sådan en kollega på."),
    ("p", "Den første fase efterlader jer med jeres filer konverteret til et kontrolleret, "
          "maskinlæsbart arkiv, som er jeres, uanset hvad I beslutter bagefter. Ejendomsporteføljer "
          "er præcis den slags papir, der før eller siden skal konverteres, og at gøre det på en "
          "lille kontrakt mod rigtige sager er den billigste måde at få det overstået på."),
    ("p", "Frida, dokumentkollegaen, er under forberedelse, og det første kundeforløb er ved at "
          "blive forberedt nu. Er det jeres branche, betyder en tidlig henvendelse, at det første "
          "arbejde formes om jeres filer."),
]

LAW_DA = [
    ("h2", "Problemet i denne branche"),
    ("p", "Sagen er arbejdet. En sag kommer med årevis af korrespondance, udkast, der ligner "
          "hinanden, et aftalebrev et sted, fakturaer, der hører til faser, og en klient, der husker "
          "en tilkendegivelse, som måske eller måske ikke står på skrift. At læse det hele er kun "
          "fakturerbart i teorien; i praksis sker det sidst på dagen, af den person, der dårligst "
          "har råd til det."),
    ("h2", "Hvad kollegaen gør med det"),
    ("ul", [
        "<b>Hele sagen, i rækkefølge.</b> Hvert dokument og hver besked i en sag, dateret, på "
        "tværs af de arkiver, sagen rører.",
        "<b>Den ordlyd, der gælder, citeret.</b> Hvilken version af en bestemmelse der er den "
        "gældende, og hvad den faktisk siger, kontrolleret ord for ord mod kilden, før I ser den.",
        "<b>Huller nævnt som huller.</b> Intet underskrevet aftalebrev, ingen skriftlig bekræftelse "
        "af en mundtlig tilkendegivelse, et manglende bilag: nævnt fra registeret over det, der "
        "blev læst.",
        "<b>Et spor, der holder.</b> Hvert udsagn bærer et link til originalen, så ræsonnementet "
        "kan efterprøves af en, der ikke var i lokalet.",
    ]),
    ("h2", "Fortrolighed og grænsen"),
    ("p", "Dokumenter behandles i Europa under en databehandleraftale med Axon Trade ApS, og "
          "supervisoren, der forbedrer kollegaen natten over, ser intet dokument og intet navn. Kun "
          "de arkiver, I tager med, læses, og intet læses, før I har sagt ja skriftligt."),
    ("p", "Kollegaen dømmer aldrig mennesker og rådgiver aldrig. Den lægger frem, hvad "
          "dokumenterne siger, og hvad de ikke siger. Den faglige vurdering bliver, hvor den hører "
          "hjemme, og det gør ansvaret også."),
    ("h2", "Sådan ville det begynde hos jer"),
    ("p", "Én afsluttet sag, I kender ud og ind, læst fra jeres eget arkiv, så I kan holde "
          "resultatet op mod det, I allerede ved. En lille første kontrakt, og I beholder det "
          "konverterede arkiv, uanset hvad I beslutter bagefter: en kontrolleret, maskinlæsbar form "
          "af jeres egne filer, som enhver AI, I tager i brug i de kommende år, alligevel får brug "
          "for, og som ingen i sidste ende slipper for at bygge."),
    ("p", "Frida er under forberedelse, og det første kundeforløb er ved at blive forberedt nu."),
]
