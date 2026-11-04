# Full case studies. Each entry adds or overrides fields on a project in data.py.
# "sections" replace the default Overview / Work / Results layout.
# Block types: p, lead, stats, media (rows of (kind, file, caption)), table (head, rows),
#              code, cards, steps, list, press, btn, quote, note

CASES = {
    "superbowl-lx": {
        "tagline": "Turning one night into 35.9M views and global press.",
        "role": "Content producer & field cast member",
        "result": "35.9M views across Instagram and TikTok · covered by TIME, People, NBC and BBC Radio 1",
        "extra_meta": [("Tools", "iPhone, CapCut")],
        "sections": [
            {"id": "overview", "label": "Overview", "h2": "I performed as a bush in Bad Bunny’s halftime show. Then I posted the day.", "blocks": [
                ("p", "I was one of the performers dressed as bushes in Bad Bunny’s Super Bowl LX halftime show. When I got home after the event, I lay on the floor for five minutes, trying to process what had just happened."),
                ("p", "Then I opened CapCut and turned the footage I already had into a GRWM (“get ready with me”) video. It went up at 11:33 PM that same night."),
            ]},
            {"id": "idea", "label": "The idea", "h2": "A one-second hook, then the whole day.", "blocks": [
                ("steps", [
                    ("0–1 s · the hook", ["Me jumping out of the grass", "“GRWM to halftime show w Bad Bunny”", "“AS A BUSH”"]),
                    ("1–30 s · the story", ["7am wash", "Getting ready", "Rehearsal & backstage", "The show", "Night"]),
                ]),
                ("p", "GRWM is a format people already know how to watch. The twist is in the caption: the person getting ready is about to become a bush on the biggest stage of the year. The text lands in the first second, before anyone can scroll away."),
                ("media", [[("img", "sb-capcut.jpg", "The edit in CapCut: the hook clip, then the day in order.")]]),
            ]},
            {"id": "results", "label": "Results", "h2": "35.9M views across Instagram and TikTok, with no paid push.", "blocks": [
                ("table", (["Metric", "Instagram", "TikTok"], [
                    ["Views", "31.4M", "4.5M"],
                    ["Likes", "2.7M", "595K"],
                    ["Shares", "692K", "24K"],
                    ["Saves", "94.3K", "26K"],
                    ["New followers", "12.4K", "2.7K"],
                    ["Avg. watch time (30 s video)", "19 s", "15.3 s"],
                ])),
                ("note", "Instagram also reached 20.7M accounts and drove 288K profile visits. On TikTok, 23% of viewers watched to the end."),
                ("media", [[("img", "sb-insights-overview.jpg", "Instagram · overview"), ("img", "sb-insights-engagement.jpg", "Instagram · engagement"), ("img", "sb-tiktok.jpg", "TikTok · key metrics")]]),
            ]},
            {"id": "press", "label": "Press", "h2": "The video turned into a news story.", "blocks": [
                ("p", "The show itself was watched by 128M viewers in the U.S. My reel was picked up by TIME, People and BBC Radio 1, and NBC Bay Area interviewed me as a halftime performer and UC Berkeley student. My audience grew to 11K+ followers, up 1,200%."),
                ("media", [[("vid", "nbc-bayarea.mp4", "NBC Bay Area: “Bad Bunny halftime ‘bush’ performers go viral”")],
                           [("img", "57mPYQUV7GavNK9KUjrijYnPdFY.jpeg", "TIME"), ("img", "02PhdzZCyVGJFwzcH9pGpXogkU.jpeg", "People")]]),
                ("press", [("TIME", "https://www.instagram.com/reel/DUlvFNeFd_N/"),
                           ("People", "https://people.com/man-dressed-as-bush-in-bad-bunny-super-bowl-halftime-show-gives-inside-look-exclusive-11903886"),
                           ("Impact", "https://www.instagram.com/p/DUuHqQglLxL/")]),
                ("btn", ("Watch the original reel", "https://www.instagram.com/reel/DUh3MNVgCon/")),
            ]},
            {"id": "takeaways", "label": "Takeaways", "h2": "What made it travel.", "blocks": [
                ("cards", [("Speed", "Posted at 11:33 PM on show night, while everyone was still talking about it."),
                           ("A known format", "GRWM needs no explanation, so the surprise does all the work."),
                           ("The hook is the caption", "“AS A BUSH” in the first second explains the whole video before anyone scrolls.")]),
            ]},
        ],
    },

    "saqa-the-spirits-of-the-three-worlds": {
        "result": "6 characters across three worlds of Sakha mythology · a 21-second fashion reel",
        "extra_meta": [("Tools", "Claude, Higgsfield, Kling, Seedance, ElevenLabs, CapCut, Final Cut Pro")],
        "sections": [
            {"id": "overview", "label": "Overview", "h2": "Sakha mythology, reimagined as haute couture.", "blocks": [
                ("p", "SAQA is an AI fashion film about the mythology of the Sakha (Yakut) people of Siberia, where I’m from. In Sakha cosmology the universe has three worlds. The film moves through them, from the white and silver of the Upper World to the ice and black of the Lower World."),
                ("p", "The character names are written in the Novgorodov alphabet, the first Sakha script (1917). It had no capital letters, and “saqa” is how “Sakha” was written in it."),
                ("media", [[("img", "saqa-kytalyk.jpg", "kytalyk — the sacred white crane, Upper World"),
                            ("img", "saqa-dyl-oguha.jpg", "dyl oguha — the Bull of Winter, detail"),
                            ("img", "saqa-abaasy.jpg", "abaasy — spirit of the Lower World, detail")]]),
            ]},
            {"id": "research", "label": "Research", "h2": "Every look starts from a real piece of Sakha dress.", "blocks": [
                ("p", "I researched traditional Sakha costume across about 60 sources, then translated each element into couture."),
                ("table", (["Element", "What it is", "How I used it"], [
                    ["Son", "Flared fur coat or kaftan with puffed shoulders and back pleats", "The base silhouette for every look"],
                    ["Taŋalai", "Archaic kaftan with short fur sleeves", "Kyys Nyurgun’s sable “wing” sleeves"],
                    ["Dyabaka", "Tall fur hat with a red crown and a silver sun", "Aiyy (cropped) and Abaasy (black)"],
                    ["Ilin / kelin kebiher", "Silver ornaments worn on the chest and back", "Sculptural breastplates"],
                    ["Bastyŋa, ytarga, kyldyy", "Headband with chains, tiered earrings, neck torque", "Chains framing the face, earrings on every character"],
                    ["Kuyakh", "Lamellar armour", "Kyys Nyurgun’s armour corset"],
                    ["Keğüör oiuu", "Lyre-shaped “tree of life” ornament", "The main motif: embroidery, engraving, Abaasy’s shield"],
                    ["Choroon, serge", "Kumis cup, hitching post", "Ritual context for Aiyy"],
                ])),
                ("cards", [("Sources", "Russian Museum of Ethnography, Yaroslavsky Yakut Museum, Churapcha Museum, and papers by Efimova, Sem, Vasiliev (2024) and Savvinov."),
                           ("Sakha designers", "muus (Lena Maximova, “kyys nyurgun”), Eikirie, ogo citizen, INNIKI, Sakhabult."),
                           ("Couture references", "Schiaparelli’s sculptural surrealism, Fecal Matter, Iris van Herpen, Rick Owens.")]),
                ("p", "What I avoided on purpose: Chukchi and Inuit parkas, reindeer, Buryat shamanic face fringe, gold and feathered headdresses. They often get mixed up with Sakha culture, and they aren’t ours."),
            ]},
            {"id": "process", "label": "Process", "h2": "A prompt formula that turns ethnography into images.", "blocks": [
                ("table", (["Stage", "Tools"], [
                    ["Research, prompts", "Claude (deep research), ChatGPT"],
                    ["Images", "Higgsfield · Nano Banana"],
                    ["Video", "Higgsfield Genjutsu (motion transfer), Kling 3.0, Seedance 2.5"],
                    ["Music", "ElevenLabs Music, Instagram library track"],
                    ["Edit", "CapCut, Final Cut Pro"],
                ])),
                ("code", "[shot type] + [Sakha model: cheekbones, frost, breath]\n+ [character from the mythology]\n+ [clothing: Sakha terms translated into visuals] + [silver & headwear]\n+ [dark studio, rim light, snow] + [palette] + [film grain, grade]\n+ [negative: Inuit parka, gold, reindeer…]"),
                ("note", "Example: dyabaka → “tall conical fur hat with a red broadcloth crown and an engraved silver sun disc”."),
                ("table", (["Round", "What changed", "Output"], [
                    ["1 · Literal", "Four looks close to tradition", "4 images"],
                    ["2 · Couture", "High-fashion rework, cropped Aiyy hat, Bull of Winter replaces the udagan", "4 images"],
                    ["3 · New characters", "Bayanai and Kytalyk added, piercings removed from the Bull", "3 images"],
                    ["4 · Details", "Two close-ups per look: face and texture", "12 images"],
                    ["5 · Khomus", "Opening shot and a fix for the grip on the mouth harp", "2 images, 2 videos"],
                    ["6 · Animation", "Kling, Seedance, Genjutsu, the wing flap", "~5 videos"],
                    ["7 · Music", "Khomus → Dune-style build → runway → crescendo", "5 prompt versions"],
                ])),
                ("p", "The edit follows a Wisdom Kaye edit set to Dune: seven cuts in 18 seconds, always detail → face → full figure."),
            ]},
            {"id": "output", "label": "Output", "h2": "A 21-second reel and six characters.", "blocks": [
                ("stats", [("6", "characters: kytalyk, aiyy, kyys nyurgun, bayanai, dyl oguha, abaasy"), ("~25", "images and ~6 videos generated"), ("7", "rounds of iteration")]),
            ]},
            {"id": "learnings", "label": "Learnings", "h2": "The first cut didn’t travel, and I know why.", "blocks": [
                ("p", "The first version of the reel opened on a still frame, and people scrolled past it. A new version opens on the wing flap, so there’s movement in the first second. It isn’t published yet."),
            ]},
        ],
    },

    "ayan": {
        "extra_meta": [("Camera", "Lumix S5II · Helios 44-2")],
        "sections": [
            {"id": "overview", "label": "Overview", "h2": "Young people from Yakutia, finding home in America.", "blocks": [
                ("p", "AYAN is an independent film about identity, belonging and the connection to one’s roots, told through young people from Yakutia building lives in the United States."),
                ("p", "I worked behind and in front of the camera: as a cinematographer and as a cast member."),
            ]},
            {"id": "camera", "label": "Cinematography", "h2": "Shot on a vintage Soviet lens.", "blocks": [
                ("p", "I shot nature and the people in the film on a Lumix S5II with a vintage Helios 44-2. The lens gives the swirling bokeh and soft flares that make the forest scenes feel like memory."),
                ("media", [[("loop", "hq3qLfhxlvKLlGSSFxDGo0MTY.mp4", ""), ("loop", "Gw6wxwT1UWLEBy5zQmBItkg970.mp4", "")],
                           [("loop", "1HLktdSOFo4FNUNlZQCtxC5ow.mp4", ""), ("loop", "cE1CydNWBv8a7zcIns7yEMrXajY.mp4", "")]]),
            ]},
            {"id": "festival", "label": "Festival", "h2": "Official Selection, Bushwick Film Festival 2026.", "blocks": [
                ("p", "In October 2026 AYAN was selected for the Bushwick Film Festival in New York City. I attended as a filmmaker and, after the screening, answered the audience’s questions in the Q&A."),
                ("media", [[("img", "ayan-qa.jpg", "Q&A after the screening"), ("img", "ayan-carpet.jpg", "Bushwick Film Festival, New York")]]),
                ("btn", ("Watch on YouTube", "https://www.youtube.com/watch?v=0tW5ulFfwrg")),
            ]},
        ],
    },

    "dwello": {
        "role": "Product designer",
        "result": "50+ high-fidelity screens across 6 end-to-end flows, plus the brand book · live pilot",
        "extra_meta": [("Timeline", "Sep 2025 – Jun 2026")],
        "sections": [
            {"id": "overview", "label": "Overview", "h2": "Finding a roommate shouldn’t mean scrolling Facebook groups.", "blocks": [
                ("p", "Dwello is a shared-housing marketplace that helps people find compatible roommates and housing quickly and safely. Users filter by budget, location and lifestyle. Detailed profiles, identity verification and roommate references reduce scams and build trust."),
                ("p", "It replaces unstructured places like Facebook housing groups and outdated roommate apps with a structured, searchable system built for fast, high-quality matches."),
                ("p", "I led design end to end, across the product and the brand: the interface, the logo and the full visual identity."),
            ]},
            {"id": "product", "label": "The product", "h2": "Listings and a live map, side by side.", "blocks": [
                ("media", [[("img", "hLTFfLN8QGmQciEYYZwc7Px3a68.png", "Search: listings next to a live map of Berkeley")],
                           [("img", "5OQy3E2f8DtgsHnkwJWDZxqHYLY.png", "Listing page: photos, price, the current tenant, amenities and location")]]),
            ]},
            {"id": "handoff", "label": "Design → dev", "h2": "Closing about 30 open questions before the mobile build.", "blocks": [
                ("p", "Before the mobile build, our developer sent me every gap they found in the desktop designs. I answered each one and added the missing screens. A few of the decisions:"),
                ("table", (["Question", "Decision"], [
                    ["Map", "Added “use my location” to request the user’s geolocation"],
                    ["Guests", "“List your room” stays in the header; tapping it opens sign in / sign up"],
                    ["Loaders", "White background with animated loaders, to match the brand"],
                    ["Errors", "One shared notification widget for sign-up errors and server errors"],
                    ["Listing", "“Apply to rent” became “Request a tour”, with a modal"],
                    ["Profile", "Your own profile gets edit controls instead of a “Message” button"],
                    ["Support", "Help & Support opens an email to customer service until there’s a help desk"],
                ])),
            ]},
            {"id": "next", "label": "What’s next", "h2": "From roommates to all of housing.", "blocks": [
                ("p", "The next roll-out adds a roommate-matching marketplace and a vacant-rentals marketplace, so Dwello covers finding roommates, searching apartments alone or together, and finding rooms for rent. Later, it grows into one marketplace for residential and commercial real estate."),
                ("btn", ("Visit the live pilot", "https://dwellopilot.com/")),
            ]},
        ],
    },

    "because-of-cltc": {
        "role": "Development coordinator · campaign identity",
        "result": "A 5-part LinkedIn video series for CLTC’s 10th anniversary, timed to Giving Tuesday",
        "sections": [
            {"id": "overview", "label": "Overview", "h2": "Ten years of impact, told by the people who lived it.", "blocks": [
                ("p", "UC Berkeley’s Center for Long-Term Cybersecurity turned ten. They wanted a short video series to celebrate the decade, reach people on LinkedIn and raise money at the end of the year. I work on CLTC’s development team. For the anniversary I designed the campaign logo and the visual identity for the series and produced the donor videos."),
            ]},
            {"id": "brief", "label": "The brief", "h2": "Short, first-person, and built to ask for support.", "blocks": [
                ("cards", [("Format", "4–5 videos under 30 seconds each, every one opening with “Because of CLTC…”."),
                           ("Voices", "First-person stories from the team and, most importantly, from students and partners."),
                           ("Timing", "Released weekly, overlapping Giving Tuesday (Dec 2) and the year-end ask (Dec 16).")]),
                ("table", (["Episode", "Story"], [
                    ["#1 · Nov 18", "Intro: public-interest cyber and the Cyber Resilience Corps"],
                    ["#2 · Nov 26", "The UC Berkeley Cybersecurity Clinic and its spread to 25 states"],
                    ["#3 · Dec 2", "Giving Tuesday: student research on privacy and AI"],
                    ["#4", "Series spotlight: everyone featured so far"],
                    ["#5 · Dec 16", "Finale with CLTC leadership and UC Berkeley Chancellor Rich Lyons"],
                ])),
            ]},
            {"id": "identity", "label": "Identity", "h2": "A serif “Because of” and a bold “CLTC”.", "blocks": [
                ("p", "The wordmark pairs an italic serif with a heavy sans: the story half and the institution half. I tested stacking, line breaks and colour on UC Berkeley navy, then layered it over halftone portraits of the people in the series."),
                ("media", [[("img", "cltc-explore-wordmarks.jpg", "Wordmark explorations on UC Berkeley navy")],
                           [("img", "cltc-explore-banners.jpg", "Cover explorations with halftone portraits")],
                           [("img", "ewrULhdOTNTXqtB7Bdm85U6jsk.png", "Final system")]]),
            ]},
            {"id": "series", "label": "The series", "h2": "", "blocks": [
                ("media", [[("vid", "ukIDi9HHqqvGDupfs5UQcxDxaI.mp4", ""), ("vid", "7dRJuWgyyMaJCAKsLeOW8zrAOwE.mp4", ""), ("vid", "DTukLo0DLIu5L7YucwXtNydKeq0.mp4", "")]]),
                ("p", "Craig Newmark reposted the donor videos, the first one without being asked."),
                ("btn", ("See the series on LinkedIn", "https://www.linkedin.com/posts/cltcberkeley_cltc-drives-impactincyber-resilience-that-activity-7396644213267947520-WQq8")),
            ]},
        ],
    },
}

CASES["expansionpictures"] = {
    "role": "President & co-founder · brand identity",
    "result": "Co-founded a 40+ member student film club with 90% retention, and designed all of its branding",
    "extra_meta": [("Timeline", "Aug 2023 – Oct 2025")],
}
CASES["ayan"]["role"] = "Cinematographer & cast member"

CASES["fallinginlove"] = {
    "role": "Visualizer · TouchDesigner",
    "result": "An audio-reactive visualizer built in TouchDesigner",
    "extra_meta": [("Tools", "TouchDesigner")],
    "sections": [
        {"id": "overview", "label": "Overview", "h2": "The rhythm of falling in love, visualized.", "blocks": [
            ("p", "“Falling in Love” is a hypnotic visualizer built around the pulse of emotion. Patterns flicker and recombine like a heartbeat learning its rhythm, pulling the viewer into the shifting, electric space of early love."),
        ]},
        {"id": "process", "label": "Process", "h2": "I started from the beat.", "blocks": [
            ("p", "The music came first. I built the piece in TouchDesigner and let the track drive it: an audio analysis of the song feeds a chain of feedback, mirroring, colour keying and bloom, so every hit of the beat pushes the pattern into a new shape."),
            ("p", "Somewhere in that motion the shapes start to look like something: a flower, a face, a heart. I never decide what. I think that’s where the art is, in the small details, where the person watching brings their own meaning to it."),
            ("media", [[("img", "fil-touchdesigner.jpg", "The TouchDesigner network: audio analysis → feedback → mirror → bloom")]]),
        ]},
    ],
}
CASES["araas"] = {"extra_meta": [("Tools", "Final Cut Pro, CapCut, Dazz Cam")]}
CASES["billieeilish"] = {"extra_meta": [("Tools", "Premiere Pro")]}

# Accent colour per project (used on hover)
ACCENTS = {'snackpass': '#16B7F2', 'saqa-the-spirits-of-the-three-worlds': '#B3121B', 'ayan': '#D9692B', 'superbowl-lx': '#4E8A2B', 'dwello': '#E4572E', 'because-of-cltc': '#002676', 'codeofbeauty': '#B76E79', 'expansionpictures': '#5B2EE0', 'roast': '#FF4A1C', 'jackal': '#3D3D3D', 'fallinginlove': '#E8452C', 'araas': '#D63A8A', 'billieeilish': '#8DB51F', 'thawing-flame': '#C8501E'}
for _k, _v in ACCENTS.items():
    CASES.setdefault(_k, {})['accent'] = _v
