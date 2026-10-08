# Inhalte der Website. Hier Texte, Projekte und Medien bearbeiten,
# danach `python3 build.py` ausführen, um die HTML-Seiten neu zu erzeugen.

SITE = {
    "name": "Ernesto Carrera",
    "title": "Ernesto Carrera | Grafikdesigner, Motion Designer und Video Editor",
    "description": "Portfolio von Ernesto Carrera, Grafikdesigner, Motion Designer und Video Editor: "
                   "Außenwerbung, Markenidentität, Bewegtbild und KI-Projekte.",
    "email": "carrera.desings@gmail.com",
    "available": "Verfügbar ab Februar 2027",
    "instagram": "https://www.instagram.com/carrera.png/",
    "behance": "https://www.behance.net/ernestojccarrera",
    "linkedin": "https://www.linkedin.com/in/ernesto-carrera-8a390327a/",
    "year": 2026,
    "url": "https://carrerapng-prog.github.io/portfolio/",
}

HERO = {
    "title": "Grafikdesign,<br>das überzeugt.",
    "text": "Strategisches Design für Print, Digital und Bewegtbild – von der Idee bis zur Umsetzung.",
    "cta": "Kontakt aufnehmen",
}

TOOLS = ["Ae", "Ai", "Ps", "Pr", "framer", "claude", "chatgpt"]

SERVICES = [
    ("billboard", "Außenwerbung & POP"),
    ("tag", "Markenidentität"),
    ("book", "Editorial & Flyer-Design"),
    ("social", "Social-Media-Design"),
    ("wand", "Bewegtbild / Motion Design"),
    ("box", "Verpackungsdesign (3D)"),
    ("layout", "Kreativberatung"),
]

ABOUT = [
    "Ich liebe es, Ideen durch Design greifbar zu machen. Was als Hobby begann, wurde zur Berufung, "
    "als ich entdeckte, wie Design nicht nur gut aussehen, sondern auch besser funktionieren kann.",
    "Mein Fokus liegt auf Markenidentität, Außenwerbung und Bewegtbild – von der ersten Skizze bis zur "
    "fertigen Umsetzung vor Ort. Ob Plakat, Rollup oder Kurzvideo: Mein Ziel ist, dass Design nicht nur "
    "gut aussieht, sondern auch beim Kunden ankommt.",
    "Bei den kleinen Dingen bin ich ein bisschen Perfektionist, denn genau das macht gutes Design für mich aus. "
    "Diese Liebe zum Detail hilft mir, starke Beziehungen zu meinen Kundinnen und Kunden aufzubauen – weil sie "
    "wissen, dass ich ihr Projekt mit derselben Sorgfalt behandle wie mein eigenes.",
]

FOOTER_WORDS = ["gestalten", "entwickeln", "erschaffen"]

# Medienblöcke: ("sheet", [teile], "...") = lange Präsentation ohne Lücken; ("img", [dateien], "Bildunterschrift") oder ("video", datei, "Bildunterschrift").
# Zwei Dateien in einer Liste = zweispaltig. "video-vertical" für Hochformat-Videos.
PROJECTS = [
    {
        "slug": "hermanos-morales",
        "name": "Hermanos Morales 88",
        "category": "Markenidentität",
        "title": "Hermanos Morales 88 — Markenidentität",
        "heading": "Hermanos Morales 88<br>— Markenidentität",
        "cover": "morales-cover.jpg",
        "client": "Hermanos Morales 88",
        "year": "2024",
        "text": [
            "Visuelle Identität für Hermanos Morales 88, einen Familienbetrieb für Wurst- und Feinkostwaren. "
            "Das Logo verbindet die Initialen HM mit einer Käsescheibe – sofort erkennbar und mit einem Augenzwinkern.",
            "Vom ersten Skizzenblatt bis zur Anwendung: Etiketten für die Verpackungen, Lieferrucksack, Schürze, "
            "Großflächenplakat und Visitenkarten. Die warme Farbpalette aus Rot, Orange und Gelb sorgt für Appetit, "
            "die Typografie (Gilroy und Fritch) für einen kräftigen, bodenständigen Auftritt.",
        ],
        "services": ["Logo-Design", "Markenidentität", "Verpackung", "Außenwerbung"],
        "link": ("Auf Behance ansehen", "https://www.behance.net/gallery/194724343/Hermanos-Morales-Identidad-Visual"),
        "media": [
            ("sheet", ["sheets/morales-1.jpg", "sheets/morales-2.jpg", "sheets/morales-3.jpg", "sheets/morales-4.jpg", "sheets/morales-5.jpg", "sheets/morales-6.jpg", "sheets/morales-7.jpg"], "Die komplette Markenpräsentation: Skizzen, Logo-Varianten, Farbpalette, "
             "Typografie und Anwendungen."),
        ],
    },
    {
        "slug": "maximus-detailing",
        "name": "Maximus Detailing",
        "category": "Markenidentität",
        "title": "Maximus Detailing — Markenidentität",
        "heading": "Maximus Detailing<br>— Markenidentität",
        "cover": "maximus-cover.jpg",
        "client": "Maximus Detailing",
        "year": "2023",
        "text": [
            "Markenidentität für Maximus Detailing, einen Service für professionelle Fahrzeugaufbereitung. "
            "Im Mittelpunkt steht ein Monogramm aus M und A, das an klassische Wappen erinnert und Hochwertigkeit "
            "ausstrahlt.",
            "Das System umfasst Wortmarke, Monogramm und Emblem und wurde auf Fahrzeugbeschriftung, Team-Shirts, "
            "Caps und Visitenkarten übertragen. Mintgrün kombiniert mit Schwarz und Grau, dazu Gilroy und Source Serif "
            "für den Kontrast zwischen modern und elegant.",
        ],
        "services": ["Logo-Design", "Markenidentität", "Fahrzeugbeschriftung", "Merchandise"],
        "link": ("Auf Behance ansehen", "https://www.behance.net/gallery/179868777/Maximus-Detailing"),
        "media": [
            ("sheet", ["sheets/maximus-1.jpg", "sheets/maximus-2.jpg", "sheets/maximus-3.jpg", "sheets/maximus-4.jpg", "sheets/maximus-5.jpg"], "Die komplette Markenpräsentation: Logo-System, Fahrzeugbeschriftung, "
             "Bekleidung, Typografie, Farben und Visitenkarten."),
        ],
    },
    {
        "slug": "braunis",
        "name": "Braunis",
        "category": "Markenidentität & Verpackung",
        "title": "Braunis — Markenidentität",
        "heading": "Braunis<br>— Markenidentität",
        "cover": "braunis-cover.jpg",
        "client": "Braunis",
        "year": "2023",
        "text": [
            "Verspielte Markenidentität für Braunis, eine kleine Brownie-Marke. Das Herzstück ist ein lachendes "
            "Gesicht, das in verschiedenen Ausdrücken auftaucht und der Marke Persönlichkeit gibt.",
            "Aus dem Charakter entstehen ein Muster, Sticker, Brownie-Boxen und Papiertüten. Die Palette aus Lila, "
            "Flieder, Sand und Mint hebt sich bewusst vom typischen Braun ab; Gilroy und eine runde Display-Schrift "
            "unterstreichen den freundlichen Ton.",
        ],
        "services": ["Logo-Design", "Markenidentität", "Verpackungsdesign", "Illustration"],
        "link": ("Auf Behance ansehen", "https://www.behance.net/gallery/175890771/Braunis-Identidad-Visual"),
        "media": [
            ("sheet", ["sheets/braunis-1.jpg", "sheets/braunis-2.jpg", "sheets/braunis-3.jpg", "sheets/braunis-4.jpg", "sheets/braunis-5.jpg"], "Die komplette Markenpräsentation: Logo, Muster, Verpackung, Sticker, "
             "Farbpalette und Typografie."),
        ],
    },
    {
        "slug": "pb-travel",
        "name": "PB Travel",
        "category": "Markenidentität",
        "title": "PB Travel — Markenidentität",
        "heading": "PB Travel<br>— Markenidentität",
        "cover": "pbtravel-cover.jpg",
        "client": "PB Travel",
        "year": "2023",
        "text": [
            "Logo und visuelle Identität für das Reisebüro PB Travel. Die Vorgabe: Rot und Weiß, modern und leicht "
            "anwendbar.",
            "Aus den ersten Skizzen entstand eine kompakte Wortmarke, in der p und b zu einem Zeichen verschmelzen. "
            "Dazu gehören Positiv- und Negativversionen, ein reduziertes Signet, Farbpalette, Typografie (Gilroy und "
            "Montserrat) sowie Anwendungen wie Leuchtschild, Website und Visitenkarten.",
        ],
        "services": ["Logo-Design", "Markenidentität", "Präsentation"],
        "media": [
            ("sheet", ["sheets/pbtravel-1-1.jpg", "sheets/pbtravel-1-2.jpg", "sheets/pbtravel-1-3.jpg", "sheets/pbtravel-1-4.jpg", "sheets/pbtravel-1-5.jpg", "sheets/pbtravel-1-6.jpg", "sheets/pbtravel-1-7.jpg", "sheets/pbtravel-1-8.jpg"], "Die komplette Markenpräsentation: Skizzen, Logo-Varianten, "
             "Farbpalette, Typografie und Anwendungen."),
        ],
    },
    {
        "slug": "der-ritter",
        "name": "Der Ritter",
        "category": "KI-Kurzfilm",
        "title": "Der Ritter — KI-Kurzfilm",
        "heading": "Der Ritter<br>— KI-Kurzfilm",
        "cover": "ritter-cover.jpg",
        "client": "Der Ritter",
        "year": "2026",
        "text": [
            "Ein kurzer KI-Film über einen Ritter: Er kommt im goldenen Abendlicht auf eine Blumenwiese, "
            "berührt die Blumen und legt sich zum Ausruhen hin – im Hintergrund eine Burg. Ein ruhiger Moment "
            "nach einer langen Reise.",
            "So bin ich vorgegangen: Zuerst habe ich eine Charakter-Referenz des Ritters erstellt, damit er in "
            "jeder Szene gleich aussieht. Die Standbilder habe ich mit Higgsfield und Claude erstellt und danach "
            "mit Magnific (Kling 3.0) animiert. Den Film habe ich in Premiere Pro geschnitten, das Making-of in "
            "After Effects gestaltet.",
        ],
        "services": ["Künstliche Intelligenz", "KI Video", "Videoschnitt", "Motion Design"],
        "media": [
            ("video", "ritter-film.mp4", "Der fertige Kurzfilm. Alle Szenen sind mit KI entstanden: Bilder mit "
             "Higgsfield, Animation mit Magnific (Kling 3.0), Schnitt in Premiere Pro."),
            ("img", ["ritter-character.jpg"], "Zuerst habe ich eine Charakter-Referenz erstellt – von vorne, von "
             "der Seite und von hinten. So sieht der Ritter in jeder Szene gleich aus."),
            ("img", ["ritter-keyframe-1.jpg", "ritter-keyframe-2.jpg"], "Zwei Keyframes aus Higgsfield. Aus diesen "
             "Standbildern habe ich danach die bewegten Szenen gemacht."),
            ("video", "ritter-making-of.mp4", "Making-of: der Weg von den Standbildern (Higgsfield und Claude) zu "
             "den animierten Szenen (Magnific, Kling 3.0), gestaltet in After Effects."),
        ],
    },
    {
        "slug": "issca",
        "name": "ISSCA",
        "category": "Motion Graphics & Video",
        "title": "Motion Graphics für den ISSCA Regenerative Medicine Summit",
        "heading": "Motion Graphics für den ISSCA Regenerative Medicine Summit",
        "cover": "issca-cover.jpg",
        "client": "ISSCA",
        "year": "2025",
        "text": [
            "Ich habe die Motion-Graphics- und Videoinhalte für den ISSCA Regenerative Medicine Global Summit 2025 "
            "sowie die ISSCA-119-Konferenz in Lissabon erstellt, darunter Live-Event-Animationen für die "
            "LED-Bühnenwände und ein vollständiges Recap-Video mit den Highlights der Sprecher und den wichtigsten "
            "Momenten der Veranstaltung.",
            "Neben den zentralen Event-Produktionen habe ich eine Reihe gebrandeter Intro-Stinger für die "
            "Online-Kursprogramme von ISSCA (Biohacking, Muse Cell und Peptidos) sowie eine Serie KI-animierter "
            "Sprecherporträts erstellt, die zur Bewerbung des Summit-Lineups in den sozialen Medien eingesetzt wurden.",
            "Dazu kamen Social-Media-Reels im Hochformat und Erklärvideos für Patientinnen und Patienten.",
        ],
        "services": ["Motion Graphics", "Videobearbeitung", "Event-Branding", "KI-unterstützte Animation"],
        "link": ("Auf Behance ansehen", "https://www.behance.net/ernestojccarrera"),
        "media": [
            ("video", "issca-speakers-lissabon.mp4", "Speaker-Präsentation für die ISSCA-119-Konferenz in Lissabon: "
             "Opener, Vorstellung der Referentinnen und Referenten und Eindrücke von der Bühne."),
            ("video", "issca-led-logo.mp4", "Logo-Animation für die Haupt-LED-Wand der Bühne im Ultra-Breitformat."),
            ("video-vertical", "issca-live-event.mp4", "Live-Aufnahmen vom ISSCA Global Summit mit den gebrandeten "
             "Opening-Titeln und Motion Graphics auf den LED-Bühnenwänden."),
            ("video", "issca-recap-1.mp4", "Auswahl an Social-Media-Reels im Hochformat – Themen wie Stammzellen, "
             "Herzgewebe und die Zertifizierung von Ärztinnen und Ärzten, gestaltet mit kinetischer Typografie."),
            ("video-vertical", ["issca-recap-speakers.mp4", "issca-speaker.mp4"], "Die Serie KI-animierter "
             "Sprecherporträts, mit denen das Lineup des Summits in den sozialen Medien beworben wurde – links die "
             "Zusammenstellung, rechts ein einzelnes Porträt."),
            ("video", "issca-recap-2.mp4", "Überblick über die Intro-Stinger der Online-Kurse Biohacking, Advanced Peptide "
             "und Advanced Muse Cell – jeweils im Quer- und Hochformat."),
            ("video", "issca-biohacking.mp4", "Gebrandeter Intro-Stinger für das Online-Kursprogramm Biohacking von ISSCA."),
            ("video-vertical", "issca-peptidos.mp4", "Gebrandeter Intro-Stinger für das Online-Kursprogramm Peptidos von ISSCA."),
            ("video", "issca-semaglutide.mp4", "Erklärvideo für Patientinnen und Patienten zur schrittweisen Dosierung "
             "von Semaglutid, mit animierten Texteinblendungen."),
        ],
    },
    {
        "slug": "sora-matcha-co",
        "name": "SORA Matcha Co.",
        "category": "KI-Branding & Bildgenerierung",
        "title": "SORA Matcha Co. — KI-Markenwelt",
        "heading": "SORA Matcha Co.<br>— KI-Markenwelt",
        "cover": "sora-cover.jpg",
        "client": "SORA Matcha Co.",
        "year": "2026",
        "text": [
            "Eine KI-generierte Markenwelt für die fiktive Matcha-Marke SORA mit drei Sorten: Matcha Clásico, "
            "Matcha Yuzu und Matcha Coco.",
            "So bin ich vorgegangen: Mit Higgsfield habe ich Produktfotos im Studio-Look und Szenen im Freien "
            "erstellt. Dazu kommen illustrierte Figuren, die als Markencharaktere mit den Bechern spielen. Die Bilder "
            "habe ich in Photoshop zusammengestellt und danach mit KI animiert. Am Ende habe ich den 15-Sekunden-Spot "
            "mit deutschen Texten in After Effects fertiggestellt.",
        ],
        "services": ["Künstliche Intelligenz", "Branding", "Bildgenerierung", "Motion Design"],
        "media": [
            ("video", "sora-spot.mp4", "Werbespot für drei neue Sorten (15 Sekunden). Die Szenen sind mit KI "
             "animiert, Texte und Schnitt habe ich in After Effects gemacht."),
            ("img", ["sora-flavors.jpg"], "Die drei Sorten der fiktiven Marke SORA: Matcha Clásico, Matcha Yuzu und "
             "Matcha Coco – mit KI erstellt und in Photoshop zusammengestellt."),
            ("img", ["sora-studio-1.jpg", "sora-studio-2.jpg"], "Produktfotos im Studio-Look, komplett mit KI erstellt (Higgsfield)."),
            ("img", ["sora-characters.jpg"], "Illustrierte Figuren als Markencharaktere, kombiniert mit realistischen "
             "Produktszenen. Diese Bilder waren die Basis für die Animationen im Spot."),
        ],
    },
    {
        "slug": "venezuela-recap",
        "name": "Venezuela Recap",
        "category": "KI-Comedy & Memes",
        "title": "Venezuela Recap — KI-Memes",
        "heading": "Venezuela Recap<br>— KI-Memes",
        "cover": "venezuela-cover.jpg",
        "client": "Venezuela Recap",
        "year": "2026",
        "text": [
            "Eine Reihe kurzer, humorvoller KI-Videos rund um die venezolanische Meme-Kultur – typische Szenen aus "
            "Venezuela, neu erzählt mit KI.",
            "So bin ich vorgegangen: Zuerst habe ich Referenzen erstellt, zum Beispiel eine Charakter-Studie für das "
            "Pferd und den leeren Laden als Ort. Dann habe ich die Szenen mit Higgsfield generiert und Details "
            "angepasst, etwa die Flasche in einer Szene. Aus den Bildern habe ich kurze Clips animiert und sie in "
            "Adobe Premiere Pro geschnitten und vertont.",
        ],
        "services": ["Künstliche Intelligenz", "KI Video", "Comedy", "Videoschnitt"],
        "media": [
            ("video", "venezuela-recap.mp4", "Kurzer Recap aus mehreren Szenen der Serie, geschnitten in Premiere Pro."),
            ("video", "venezuela-horse.mp4", "Eine Szene der Serie: ein weißes Pferd im Supermarkt, aus einem KI-Bild animiert."),
            ("img", ["venezuela-horse-study.jpg", "venezuela-store.jpg"], "Vorbereitung: eine Charakter-Studie für das "
             "Pferd und der leere Laden als Ort. Danach habe ich beides in einer Szene kombiniert."),
            ("img", ["venezuela-moto.jpg", "venezuela-taxi.jpg"], "Weitere Szenen der Serie: eine Motorrad-Show im Barrio und eine Taxifahrt."),
            ("img", ["venezuela-before.jpg", "venezuela-after.jpg"], "Vorher und nachher: Die Flasche habe ich separat "
             "erstellt und im Bild statt des Glases eingesetzt."),
        ],
    },
    {
        "slug": "novita-muebles",
        "name": "Novita Muebles",
        "category": "Außenwerbung & POP-Material für Novita Muebles",
        "title": "Außenwerbung & POP-Material für Novita Muebles",
        "heading": "Außenwerbung &amp;<br>POP-Material für<br>Novita Muebles",
        "cover": "novita-cover.jpg",
        "client": "Novita Muebles",
        "year": "2023–2024",
        "text": [
            "Außenwerbung und Rollup-Displays für Novita Muebles, eine Möbelkette mit Standorten in Valencia, "
            "Caracas, Barquisimeto und Maracaibo (Venezuela). Die Kampagne bewarb die Marken Artie und Trimmel im "
            "öffentlichen Raum und am Verkaufsort – von Großflächenplakaten an stark befahrenen Straßen bis zu "
            "Roll-up-Bannern im Showroom.",
        ],
        "services": ["Außenwerbung", "POP-Material"],
        "media": [
            ("img", ["novita-rollup-artie.jpg", "novita-rollup-trimmel.jpg"], "Roll-up-Banner im Showroom für die Marken Artie und Trimmel."),
            ("img", ["novita-billboard-higold.png"], "Großflächenwerbung an einer Ausfallstraße, Sortiment „Higold“."),
            ("img", ["novita-caracas.jpg"], "Straßenszene in Caracas mit Werbetafel im Hintergrund."),
            ("img", ["novita-cover.jpg"], "Bauzaun-Werbebanner in Naguanagua, Valencia – das auffälligste Motiv der Kampagne."),
        ],
    },
]

# Gruppen (Reihenfolge = Reihenfolge auf der Website).
# "home": auf der Startseite zeigen; "heading": (grauer Teil, schwarzer Teil) der Überschrift.
GROUPS = [
    {"id": "projekte", "home": True, "heading": ("Ausgewählte", "Projekte"),
     "slugs": ["novita-muebles", "issca"]},
    {"id": "branding", "home": True, "heading": ("Branding", "Marken mit Charakter."),
     "slugs": ["hermanos-morales", "maximus-detailing", "braunis", "pb-travel"]},
    {"id": "ki", "home": False, "heading": ("KI-Projekte", "Experimente mit KI."),
     "slugs": ["der-ritter", "sora-matcha-co", "venezuela-recap"]},
]

# Bilder im Kartenstapel oben auf der Startseite
HERO_STACK = ["novita-muebles", "issca", "hermanos-morales", "maximus-detailing"]
ALL_PROJECTS = [slug for g in GROUPS for slug in g["slugs"]]
