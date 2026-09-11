"""Product and policy copy for saasquatchlab.com.

Keep this in sync with what actually ships — status tags here drive the site.
"""

APPSTORE = "https://apps.apple.com/app/id"

PRODUCTS = [
    dict(
        slug="sasquatch-social", name="Sasquatch Social", accent="#40916c",
        logo="logo-sasquatch-social.png", tag="Live", tagclass="live",
        category="Social network",
        tagline="A social network built for conversation, not compulsion.",
        blurb=("A community-first social network built around real conversation, local "
               "connection, and civic engagement — without the algorithmic manipulation "
               "and engagement traps of mainstream platforms."),
        meta=["Verified real identities", "The Agora debate platform", "Marketplace, hiring &amp; events", "iOS and web"],
        hero_note="Free to join &middot; iOS and web &middot; Identity verification optional",
        ctas=[("Open Sasquatch Social", "https://www.sasquatchsocial.com", "primary", True),
              ("Download on the App Store", APPSTORE + "6762406901", "ghost", True)],
        promise=("Sasquatch Social is the one product that necessarily stores what you post — it is a "
                 "social network. It still runs <strong>no advertising SDKs and no cross-app trackers</strong>, "
                 "and identity verification returns a pass or fail without us ever holding your ID."),
        features=[
            ("A feed you control", "Local, regional, and topical sections you choose between — plus filters, mutes, and blocks that actually stick. No engagement-optimised ranking deciding what you care about."),
            ("The Agora", "A structured debate space for civic argument. Topics are framed, positions are stated, and threads are built for reasoning rather than dunking."),
            ("Verified people", "Optional identity verification through our KYC provider. Verified members show a real legal name, so you know you are arguing with a person, not a farm."),
            ("Marketplace &amp; hiring", "Buy and sell locally, post jobs, and run a hiring fair — inside the same community, without a separate account."),
            ("Events &amp; blogs", "Organise events, publish long-form writing, and keep a local calendar that neighbours can actually find."),
            ("Business profiles", "Verified business accounts with KYB checks, so local businesses can participate without impersonation risk."),
            ("Dating, only if you want it", "A dating section that stays completely switched off unless you deliberately enable it. No surprise matchmaking."),
            ("Moderation with reasons", "Report, mute, and block tools, plus a &ldquo;why am I seeing this?&rdquo; explanation on posts. Moderation decisions come with reasoning."),
        ],
        detail=[("Built on the same principles as everything else",
                 ["Sasquatch Social runs on infrastructure we operate, with row-level authorisation so members can only reach their own data. There is no ad network embedded in the app, no data broker relationship, and no behavioural profile being assembled in the background.",
                  "Identity verification is handled by a dedicated provider. They check the document; we receive a result and, if you pass, your verified legal name. Images of your ID never reach our servers. You can use a nickname publicly and keep your legal name as secondary context."])],
    ),
    dict(
        slug="squatch-lift", name="Squatch Lift", accent="#74c69d",
        logo="logo-squatchlift.png", tag="In App Review", tagclass="review",
        category="Fitness &middot; iOS &amp; Android",
        tagline="Log the set. Close the phone.",
        blurb=("A no-nonsense workout tracker built for the gym floor. Log lifts in seconds "
               "between sets, watch strength trend upward, and keep every rep on your device — "
               "your training data never touches a server."),
        meta=["130+ exercise library", "Personal record tracking", "No accounts, no tracking", "iPhone, iPad &amp; Android"],
        hero_note="Three full workouts free &middot; Pro $4.99/month or $29.99/year &middot; No account, ever",
        ctas=[("Coming to the App Store", "#", "primary", False)],
        promise=("Squatch Lift has <strong>no servers of its own</strong>. Your workouts, measurements, "
                 "and photos live in a database on your phone, and we could not see your training "
                 "data if we wanted to. On iPhone and iPad the app makes no network requests at all; "
                 "on Android, Google&rsquo;s billing library needs network permission to process the "
                 "subscription, and that is the only thing it is used for."),
        features=[
            ("Fast set logging", "Weight, reps, and done. The last workout prefills automatically, so repeating a session is a few taps rather than a data-entry chore."),
            ("130+ exercise library", "A full catalogue out of the box, plus your own custom movements. Templates cover standard training splits, with beginner suggestions you can switch off once you outgrow them."),
            ("Live PR badges", "Personal records surface the moment you beat them — mid-workout, while it still feels good."),
            ("Strength trends", "History and charts that show whether the last two months actually moved anything, per lift."),
            ("Body measurements", "Track weight and measurements over time on the same charts as your lifts, so you can see the whole picture."),
            ("Supplement log", "A simple record of what you are taking and when, kept alongside the training it belongs to."),
            ("Share cards", "Render a clean workout summary card — optionally with a selfie — to post wherever you like. You choose what leaves the phone."),
            ("Pounds or kilos", "Weights are stored canonically and converted for display, so switching units never corrupts your history."),
        ],
        detail=[("Pricing", [
            "Your first three completed workouts are free, with no account and no card. After that, Squatch Lift Pro unlocks unlimited use at <strong>$4.99 per month</strong> or <strong>$29.99 per year</strong>.",
            "Subscriptions are billed by Apple and renew automatically until cancelled. You manage or cancel from your App Store account settings at any time — full terms are in our <a href=\"/terms#subscriptions\">Terms of Use</a>."]),
            ("On Android", [
                "The Android build carries the same 130+ exercise catalogue, the same fast set logging, the same PR badges and strength charts, and the same three-free-workouts-then-Pro pricing as the iPhone version. Your training data is stored on the device there too.",
                "One honest difference: Google&rsquo;s billing library requires network permissions in order to sell and verify the subscription, so the Android build declares them. Nothing about your training is sent anywhere — the network is used only for the purchase."])],
    ),
    dict(
        slug="sizesquatch", name="SizeSquatch", accent="#a5dcc0",
        logo="logo-sizesquatch.png", tag="Live", tagclass="live",
        category="Photo utility &middot; iOS &amp; Android",
        tagline="Any photo. Perfect size.",
        blurb=("Resize any photo to exactly the right size for wherever it is going — Instagram, "
               "LinkedIn, ads, prints, even passport photos. Every pixel is processed on your "
               "device: your photos never leave your phone."),
        meta=["45+ built-in presets", "Passport &amp; ID sizing", "Exact file-size targets", "100% on-device"],
        hero_note="Free to try &middot; three free exports &middot; $4.99 one-time unlock &middot; No subscription",
        ctas=[("Download on the App Store", APPSTORE + "6806940474", "primary", True)],
        promise=("<strong>Your photos never leave your device.</strong> All resizing and encoding happens "
                 "locally, and SizeSquatch has no server of its own to send anything to. It uses the system "
                 "photo picker, so it can only ever touch the specific photos you hand it — never your "
                 "whole library."),
        features=[
            ("Every size you need", "Presets for Instagram, Facebook, LinkedIn, X, YouTube, TikTok, and Pinterest, plus IAB display ad sizes and social and CTV creative formats."),
            ("Print at 300 DPI", "Real print sizes with the DPI metadata actually embedded in the file, so the lab prints what you meant."),
            ("Passport &amp; ID photos", "US 2&times;2&Prime; and UK/EU sizes with the official framing rules built in, and instructions on screen while you crop."),
            ("Frame it yourself", "Drag and pinch to position the crop. The frame is clamped so circular and fill exports can never come out with a surprise white bar."),
            ("Hit an exact file size", "Set a KB or MB ceiling and SizeSquatch searches for the highest quality that fits underneath it."),
            ("Photo grids", "Build multi-photo grids at the exact output size you need, without a separate collage app."),
            ("JPEG, PNG, HEIC", "Pick your format, or let &ldquo;Auto — best for target&rdquo; choose. Defaults are configurable in Settings so you are not re-picking every time."),
            ("Custom pixel sizes", "Any width and height you like, when none of the presets are the thing you actually need."),
        ],
        detail=[("Pricing", [
            "SizeSquatch is free to download and gives you three free exports. A single <strong>$4.99 one-time unlock</strong> removes the limit permanently. There is no subscription and there never will be."]),
            ("On Android", [
                "SizeSquatch on Android carries the same preset catalogue, the same fit and fill editor with circular crops, the same maximum-file-size search, and the same three-free-exports-then-one-unlock pricing as the iPhone version. One honest difference: Google's billing library requires network permissions in order to process the unlock, so the Android build declares them. No photo is ever sent anywhere — the network is used only to check and complete your purchase."])],
    ),
    dict(
        slug="squatch-connect", name="Squatch Connect", accent="#52b788",
        logo="logo-squatch-connect.png", tag="In App Review", tagclass="review",
        category="Travel eSIM &middot; iOS &amp; Android",
        tagline="Data abroad without the surveillance.",
        blurb=("A privacy-first travel eSIM. Pick a destination, pick a plan, and install in one "
               "tap — or just ask Siri. No account, no tracking, no passport uploads."),
        meta=["No account required", "One-tap eSIM install", "Live usage widgets", "Apple Pay checkout"],
        hero_note="Plans from $1.99 &middot; No account &middot; No subscription &middot; Pay as you travel",
        ctas=[("Coming to the App Store", "#", "primary", False)],
        promise=("Squatch Connect has <strong>no user accounts at all</strong>. We process the destination "
                 "you picked and an email for your receipt. Stripe handles the payment; we never see "
                 "your card. There is no passport upload and no KYC."),
        features=[
            ("Pick a destination", "Countries and regions, each with plans sized for a weekend or a month. Prices are shown before you commit, with no conversion games at checkout."),
            ("One-tap install", "On iOS 17.4 and later the eSIM installs through Apple&rsquo;s own provisioning link — no QR gymnastics. QR and manual entry are always available as fallbacks."),
            ("Ask Siri", "&ldquo;Hey Siri, add an eSIM for France in Squatch Connect.&rdquo; App Shortcuts cover every destination we sell."),
            ("Live usage", "A gauge showing exactly how much data is left and when the plan expires, refreshed when you open the app or pull to refresh."),
            ("Home and lock screen widgets", "Data remaining on your home screen and lock screen, kept current in the background so you can check without unlocking."),
            ("Hotspot-ready plans", "Tiers that permit tethering, for when the laptop needs to come online too."),
            ("Honest about locks", "We warn you before purchase if your device may be carrier-locked, because an eSIM you cannot install is not a bargain."),
            ("Guest checkout", "Apple Pay or card through Stripe, with no account to create and no password to forget."),
        ],
        detail=[("What an eSIM is and is not", [
            "Squatch Connect sells cellular data plans that install as an eSIM profile on your phone. It gives you working mobile data abroad at local rates instead of your carrier&rsquo;s roaming price.",
            "It is a connectivity product, not a privacy tunnel — it does not encrypt or anonymise your traffic beyond what normal cellular service does. We would rather tell you that plainly than let you assume otherwise."]),
            ("Android", ["A native Android build is in <strong>internal testing on Google Play</strong>, with the same catalogue, the same install flow, and a home screen widget that refreshes in the background."])],
    ),
    dict(
        slug="squatchtravel", name="Squatch Travel", accent="#E07A5F",
        logo="logo-squatch-travel.png", tag="In App Review", tagclass="review",
        category="Travel companion &middot; iOS",
        tagline="Everything you need, before you lose signal.",
        blurb=("One app from booking to touchdown: itinerary, offline translation, emergency "
               "numbers, currency, and local know-how — all downloaded before you fly, so "
               "everything works with no cell service."),
        meta=["Works fully offline", "29-language phrasebook", "66 destination packs", "On-device translation"],
        hero_note="$4.99 per trip, or $29.99/year for unlimited trips",
        ctas=[("Coming to the App Store", "#", "primary", False)],
        promise=("Your itinerary, documents, and health information stay <strong>on your device</strong>. "
                 "Destination packs are fetched with a two-letter country code and nothing else — "
                 "we cannot tell who asked, or when you are travelling."),
        features=[
            ("Your itinerary, offline", "Reservations, seat numbers, and gates two taps away, with no signal and no loading spinner."),
            ("29-language phrasebook", "Downloaded before you go, plus translated allergy and medication cards for the conversations you really cannot afford to fumble."),
            ("On-device translation", "Live translation runs through Apple&rsquo;s own on-device models. No third-party translation SDK, no sentences sent to a server."),
            ("Emergency briefings", "Local emergency numbers, customs notes, and safety guidance for every destination, kept with the trip."),
            ("Live currency", "Exchange rates refreshed when you download or verify a pack, then frozen offline so the numbers still work on the plane."),
            ("Luggage tracking", "A reusable bag library you assign to each trip, with airline tag numbers, barcode scanning, AirTag hand-off to Find My, and NFC tag import."),
            ("Apple Wallet health card", "A health card pass built on your device and added to Wallet — the content never leaves the phone, only a hash is signed."),
            ("Trips that age gracefully", "Edit a trip before departure, extend it mid-journey, and archive it afterwards so old trips stop nagging you."),
        ],
        detail=[("Pricing", [
            "Squatch Travel is <strong>$4.99 per trip</strong>, or <strong>$29.99 per year</strong> for unlimited trips. Buy a single trip if you travel once a year; take the annual plan if you do not."]),
            ("Built-in eSIM", ["Squatch Travel connects to Squatch Connect, so you can add mobile data for your destination from inside your itinerary rather than hunting for a SIM at the airport."])],
    ),
    dict(
        slug="squatch-vitals", name="Squatch Vitals", accent="#2d6a4f", for_good=True,
        logo="logo-squatch-vitals.png", tag="In App Review", tagclass="review",
        category="Health tracking &middot; iOS",
        tagline="Your numbers, in one place, on your phone.",
        blurb=("A daily record of weight, blood pressure, blood oxygen, heart rate and sleep, "
               "built for someone who has been asked to keep track and hand it to a doctor. "
               "Photograph a paper log and it reads the numbers off the page. Everything stays "
               "on the phone."),
        meta=["Weight against a goal", "Reads your paper log sheet", "Apple Watch import", "PDF report for your doctor"],
        hero_note="Free &middot; No account &middot; Nothing leaves your iPhone unless you send it",
        ctas=[("Coming to the App Store", "#", "primary", False)],
        promise=("Squatch Vitals contains <strong>no networking code at all</strong> &mdash; no account, no "
                 "server, no analytics. Apple Health access is <strong>read-only</strong>, so the app "
                 "structurally cannot alter your Health record. The only way a reading leaves the phone "
                 "is when you send a report yourself."),
        features=[
            ("Daily weight against a goal", "Every weigh-in shows how far above or below your goal you are, and what changed since last time. Log more than once a day when your care team asks for it."),
            ("Blood pressure and blood oxygen", "As many readings a day as you need, each one placed against the standard reference ranges so a high number is obvious at a glance."),
            ("Sleep from your Apple Watch", "Time asleep, time in bed, sleep efficiency, deep and REM &mdash; pulled from what your watch already recorded, or typed in by hand."),
            ("Scan a paper log sheet", "Photograph the handwritten sheet on the fridge and Squatch Vitals reads the dates and numbers off it. You check every row before anything is saved."),
            ("Trends that answer the question", "Week, month, quarter, year. Whether the last two months actually moved anything, with your goal drawn on the chart."),
            ("A report your doctor can read", "A clean PDF &mdash; summary page, then day-by-day detail &mdash; or CSV for a spreadsheet. Any date range, sent by email, message, AirDrop or Files."),
            ("A nudge in the morning", "One local notification at a time you pick, so the record does not develop holes."),
            ("Only what you need", "Switch off anything you are not tracking and it leaves the screen. Readings you already recorded are never hidden."),
        ],
        detail=[("Built for a patient, not a fitness tracker", [
            "The reason this exists is unglamorous: someone is asked to write their weight and blood pressure on a piece of paper every morning and bring it to an appointment. Paper gets lost, handwriting gets misread, and nobody can see a trend in a column of numbers.",
            "So the app is deliberately plain. Big targets, a goal you can see, and a report that prints. It does not score you, gamify anything, or tell you what your readings mean &mdash; it is a record-keeping tool, not a medical device, and it says so on every screen that shows a reference range."]),
            ("Why it reads your paper sheet", [
                "Months of existing readings are usually already on paper, and retyping them is exactly the sort of chore that stops someone using an app at all. Squatch Vitals uses Apple&rsquo;s on-device text recognition to read the page &mdash; the photo is processed in memory, never written to disk, and never uploaded.",
                "Nothing is trusted blindly. Every row it reads is shown next to the raw line it came from, dates it had to guess are flagged, and any line holding a number it could not interpret is reported rather than silently dropped."])],
    ),
    dict(
        slug="squatch-aphantasia", name="Squatch Aphantasia", accent="#4f86c6",
        logo="logo-squatch-aphantasia.png", tag="Coming soon", tagclass="soon", for_good=True,
        category="Education &amp; accessibility &middot; iOS &amp; iPadOS",
        tagline="What do you need to visualize?",
        blurb=("Paste it, photograph it, or scan it. Squatch explains it without asking you to "
               "picture anything."),
        meta=["No mental imagery required", "Persistent Learning Board", "Ask Squatch tutor", "Free, no account, no ads"],
        hero_note="Free &middot; No account required &middot; No ads &middot; For students 13+",
        ctas=[("Coming to the App Store", "#", "primary", False)],
        promise=("You don&rsquo;t have to picture it to understand it. Squatch Aphantasia asks for nothing "
                 "but the material you want explained &mdash; <strong>no account, no ads, no data sale</strong>. "
                 "Everything you save stays on your device; the only thing that ever leaves it is the material "
                 "you choose to have explained, sent only to generate that explanation."),
        features=[
            ("Any material in", "Type it, paste it, photograph a textbook page, scan a worksheet, or hand over a PDF &mdash; Squatch Aphantasia reads it however it arrives."),
            ("Press &ldquo;I Can&rsquo;t Picture This&rdquo;", "Whenever an explanation leans on an image you can&rsquo;t form, tap the I Can&rsquo;t Picture This button and Squatch rewrites that part in words, structure, and logic instead &mdash; no picturing required."),
            ("The main idea, stated plainly", "Each explanation opens with what it is actually about, in one sentence you can hold onto before the detail arrives."),
            ("Facts kept visible", "Key facts stay on screen as you work through the material, so nothing depends on remembering something you were never shown a picture of."),
            ("Steps in order, relationships made explicit", "Processes are broken into ordered steps, and how ideas connect to each other is stated outright &mdash; never left for you to visualise."),
            ("A Learning Board that persists", "A running board of concrete examples and key facts for what you are studying, saved and ready next time you open it &mdash; even offline."),
            ("Read-aloud audio &amp; Ask Squatch", "Have the material read aloud, or ask Squatch, the built-in tutor, a follow-up question when a part still hasn&rsquo;t landed."),
            ("Quizzes with Need Help", "Check what stuck, and tap Need Help mid-quiz for a nudge that never relies on picturing the answer."),
        ],
        detail=[("Who it&rsquo;s for", [
            "Squatch Aphantasia is built for students 13 and up &mdash; high school, college, and adult learners &mdash; who have aphantasia or otherwise weak mental imagery, and who are tired of material that leans on &ldquo;picture this&rdquo; as if it were the only way in.",
            "It is an <strong>educational accessibility tool, not a diagnosis or a treatment</strong>. It does not assess or label anyone; it explains material in a way that never depends on forming a mental image."]),
            ("Works offline once saved", [
                "Explanations, Learning Boards, quizzes, and tutor conversations are saved to the device and stay usable with no connection. The app is free, requires no account, and carries no ads &mdash; and there are no upsells waiting once you are in."])],
    ),
    dict(
        slug="app-tracker", name="App Tracker", accent="#3a6478",
        logo=None, emoji="&#128203;", tag="Live", tagclass="live",
        category="Career tools &middot; Web",
        tagline="Know exactly what you told every employer.",
        blurb=("A job application manager built around a resume vault and an append-only "
               "consistency ledger — so months into a search you still know which version of "
               "your story went where."),
        meta=["Resume vault", "Consistency ledger", "AI writing suite", "LinkedIn import"],
        hero_note="Free to start &middot; Pro $9/month or $79/year",
        ctas=[("Open App Tracker", "https://saasquatchapptracker.com", "primary", True)],
        promise=("App Tracker stores the applications and documents you create so they follow you "
                 "across devices. <strong>We never share your job search</strong> with employers, "
                 "recruiters, or anyone else."),
        features=[
            ("Resume vault", "Versioned resume variants, kept properly rather than as a folder of near-identical files with dates in the name."),
            ("Consistency ledger", "An append-only record of which resume, which claims, and which answers went to which employer — so you never contradict yourself in round three."),
            ("Application pipeline", "Every application with its status, next step, and reminders, so nothing quietly dies in your inbox."),
            ("AI writing suite", "Draft tailored resumes, cover letters, and thank-you notes against a specific posting, starting from what is already in your vault."),
            ("Resume workspace", "Live preview and clean PDF export, so what you send is what you saw."),
            ("LinkedIn import", "Bring your history in from a LinkedIn export rather than retyping a decade of roles."),
            ("Company intel", "Background and prep material for interviews, gathered per employer."),
            ("Honest multi-tracking", "Built on the assumption that you are pursuing several things at once, and that managing that honestly is the actual hard part."),
        ],
        detail=[("Pricing", ["App Tracker is free to start. Pro is <strong>$9 per month</strong> or <strong>$79 per year</strong>, billed through Stripe on the web — not through an app store."])],
    ),
]

FOR_GOOD_SLUGS = ["squatch-vitals", "squatch-aphantasia"]

FOR_GOOD_SHORT = (
    "Sasquatch for Good is a small, separate family of apps built to help, not to make money. Every app in "
    "it is <strong>free</strong>, asks for no account, carries no ads, and sells no data &mdash; and there is "
    "no upsell waiting once you are in, because that was never the plan."
)

FOR_GOOD_FULL = [
    "Sasquatch for Good is a small, separate family of apps built to help, not to make money. Every app in "
    "it is <strong>free</strong>, asks for no account, carries no ads, and sells no data &mdash; and there is "
    "no upsell waiting once you are in, because that was never the plan.",
    "Everything else about how we build &mdash; privacy-first design, no ad trackers, no data brokers, no "
    "dark patterns &mdash; already applied to these apps before this family had a name. What sets them apart "
    "is the reason they exist: someone needed a tool that did not exist yet, or existed only behind a "
    "paywall, and building it was the whole point.",
    "If you or someone you know could use one of these, or you have an idea for a tool that belongs in this "
    "family, we would like to hear it. Email <a href=\"mailto:hello@saasquatchlab.com\">hello@saasquatchlab.com</a>.",
]

COMING = dict(
    slug=None, name="Sasquatch Polling", accent="#c07b3a", emoji="&#128202;",
    tag="Coming soon", tagclass="soon", category="Polling platform",
    blurb=("A transparent polling platform for media organisations, campaigns, and civic groups — "
           "live results, demographic breakdowns, embeddable widgets, and a published methodology. "
           "It is deliberately on hold: credible polling needs a real respondent base, so Polling "
           "launches once Sasquatch Social has the community to support it."),
    meta=["Not yet in use", "Waiting on Sasquatch Social scale"],
)


POLICIES = {
    "squatch-lift": dict(
        name="Squatch Lift", accent="#74c69d",
        short="Squatch Lift collects nothing. It has no servers, and no copy of your training data exists anywhere but your device.",
        sections=[
            ("What we collect", [
                "<strong>Nothing.</strong> Squatch Lift has no backend, no user accounts, no analytics, no advertising SDKs, and no third-party trackers.",
                "On iPhone and iPad the app makes no network connections of its own. On Android, Google Play&rsquo;s billing library requires network permissions in order to sell and verify the subscription, so the Android build declares them; they are used for nothing else. No training data, photo, or measurement is transmitted on either platform."]),
            ("Your training data", [
                "Your workouts, exercise history, personal records, body measurements, supplement log, custom exercises, and templates are stored in a database <strong>on your device</strong> — Apple&rsquo;s on-device storage framework on iPhone and iPad, and the equivalent on-device database on Android.",
                "This data is never transmitted to us or to anyone else. We have no copy of it and no way to obtain one. If you delete the app, the data is deleted with it, so keep a device backup if you want to preserve your history."]),
            ("Photos", ["If you attach a selfie to a workout share card, the image is used only to render that card on your device. It is not uploaded. Where the resulting card goes afterwards is entirely your choice."]),
            ("Health data", ["Squatch Lift does not read from or write to Apple Health. The measurements you enter are typed by you and stay in the app."]),
            ("Subscriptions", [
                "Squatch Lift Pro is an auto-renewing subscription ($4.99/month or $29.99/year), sold through Apple on iPhone and iPad and through Google Play on Android. <strong>The store processes the payment; we never receive your card details or your Apple or Google account identity.</strong> The app receives only a signed receipt confirming whether a subscription is active, and it validates that on your device.",
                "Manage or cancel from your App Store account settings, or from Google Play&rsquo;s subscriptions screen on Android. Full terms are in our <a href=\"/terms#subscriptions\">Terms of Use</a>."]),
            ("What we never do", ["We do not sell data, share it with data brokers, or use it for advertising — a claim that is easy for us to make, because the data never leaves your phone."]),
            ("Children", ["Squatch Lift is not directed to children under 13 and collects no personal information from anyone."]),
            ("Your rights", ["Rights to access, correct, delete, or port your data apply to data a company holds about you. We hold none. Deleting the app removes everything. If you have questions, email <a href=\"mailto:hello@saasquatchlab.com\">hello@saasquatchlab.com</a>."]),
        ]),
    "squatch-vitals": dict(
        name="Squatch Vitals", accent="#2d6a4f",
        short=("Squatch Vitals collects nothing. It has no servers and contains no networking code, "
               "Apple Health access is read-only, and your readings exist only on your iPhone."),
        sections=[
            ("What we collect", [
                "<strong>Nothing.</strong> Squatch Vitals has no backend, no user accounts, no analytics, no advertising SDKs, and no third-party trackers.",
                "The app contains <strong>no networking code at all</strong>. It cannot transmit a reading because it has nothing to transmit to and no means of doing so. Squatch Vitals is iPhone and iPad only; there is no Android build and therefore no billing library requiring network permissions."]),
            ("Your health readings", [
                "Your weight and goal, blood pressure, blood oxygen, heart rate, sleep, fluid intake, notes, and reminder settings are stored in a database <strong>on your device</strong> using Apple&rsquo;s on-device storage framework.",
                "This data is never transmitted to us or to anyone else. We have no copy of it and no way to obtain one. If you delete the app, the data is deleted with it, so keep a device backup if you want to preserve your history."]),
            ("Apple Health", [
                "Squatch Vitals requests <strong>read permission only</strong>. It is not capable of writing to or changing your Health record &mdash; the request for write access is empty, so iOS will not grant it.",
                "It reads heart rate, blood oxygen, blood pressure, body weight and sleep, and only when you run an import and choose what to bring in. You see every reading before it is saved, and you can decline any of it. What it reads stays on the device alongside everything else.",
                "You can revoke Health access at any time in Settings &rsaquo; Privacy &amp; Security &rsaquo; Health &rsaquo; Squatch Vitals. The app keeps working; it simply stops importing."]),
            ("Camera and photos", [
                "The camera and photo library are used for one thing: reading a photograph of a paper log sheet. Text recognition runs <strong>entirely on your device</strong> using Apple&rsquo;s Vision framework.",
                "The image is processed in memory and is never written to disk, never stored in the app, and never uploaded. Choosing an existing photo goes through the system photo picker, so the app only ever sees the single image you hand it &mdash; never your library."]),
            ("Reports you send", [
                "PDF and CSV reports are generated on your device into temporary storage, and the previous export is deleted each time a new one is made.",
                "A report leaves your phone only when <strong>you</strong> send it, through the system share sheet, to a destination you pick &mdash; email, Messages, Files, AirDrop or a printer. We are not a party to that and never receive a copy."]),
            ("Reminders", ["The morning weigh-in reminder is a local notification scheduled on your device. Nothing is registered with a push server and no reminder passes through us."]),
            ("Price", ["Squatch Vitals is free. There is no subscription, no in-app purchase, and no payment processing of any kind."]),
            ("Not a medical device", ["Squatch Vitals is a personal record-keeping tool. It does not diagnose anything, and the reference ranges it displays are general published bands shown for context only. It is not a substitute for advice from your care team."]),
            ("What we never do", ["We do not sell data, share it with data brokers, or use it for advertising &mdash; a claim that is easy for us to make, because the data never leaves your phone."]),
            ("Children", ["Squatch Vitals is not directed to children under 13 and collects no personal information from anyone."]),
            ("Your rights", ["Rights to access, correct, delete, or port your data apply to data a company holds about you. We hold none. Deleting the app removes everything. If you have questions, email <a href=\"mailto:hello@saasquatchlab.com\">hello@saasquatchlab.com</a>."]),
        ]),
    "sasquatch-social": dict(
        name="Sasquatch Social", accent="#40916c",
        short=("Sasquatch Social stores what you post, because it is a social network. It runs no "
               "advertising trackers, sells nothing, and never holds images of your ID."),
        sections=[
            ("What we collect", [
                "<strong>Account information</strong> — your email address and a password stored as a hash, plus the profile details you choose to add (nickname, bio, avatar, location preferences).",
                "<strong>Content you create</strong> — posts, comments, debate contributions, messages, marketplace listings, job posts, events, blog entries, poll votes, and any media you upload.",
                "<strong>Social graph</strong> — accounts you follow, block, or mute, and the communities you join.",
                "<strong>Operational logs</strong> — the minimum server-side records needed to keep the service running, prevent abuse, and investigate reports."]),
            ("Identity verification", [
                "Verification is optional. If you choose to verify, our verification provider (Didit, with Stripe Identity as a fallback) collects and checks your government ID directly under its own privacy policy.",
                "<strong>We never receive or store images of your identity document.</strong> The provider returns a pass or fail result and, on success, your verified legal name. You can display a nickname publicly instead, with your verified name shown as secondary context.",
                "Business verification (KYB) works the same way for business profiles."]),
            ("Dating", ["Dating features are disabled unless you explicitly enable them. When off, no dating profile exists and no dating data is collected. Turning the feature off again stops further processing."]),
            ("Payments", ["Purchases, subscriptions, and advertising credits are processed by Stripe. <strong>We never see or store your card number.</strong> We keep only the record that a payment succeeded."]),
            ("Video calls", ["Video calling is provided by Twilio. Call media is routed by Twilio under its own terms; we do not record calls."]),
            ("How we use it", [
                "To operate the service, show you the feed and sections you asked for, deliver notifications you opted into, keep the platform safe, and comply with law.",
                "<strong>We do not build advertising profiles from your activity</strong>, we do not embed third-party ad or analytics SDKs in the app, and we do not sell or rent your information."]),
            ("Advertising", ["Where advertising appears, it is sold by us and targeted at most by broad context — not by cross-app tracking or a behavioural profile assembled about you. Advertisers receive aggregate performance figures, never your identity."]),
            ("Who can see what", ["Public posts are public. Content posted to a limited community is visible to that community. Direct messages are visible to their participants. Moderators and administrators can access content that has been reported, in order to act on it."]),
            ("Retention", ["We keep your content while your account is open. When you delete your account, your content is removed within 30 days, except where we must retain records to comply with law or resolve a dispute. Operational logs roll off on a short schedule."]),
            ("Your rights", [
                "You can access, correct, export, or delete your data. Sasquatch Social has in-app tools at <a href=\"https://www.sasquatchsocial.com/privacy/data-rights\">sasquatchsocial.com/privacy/data-rights</a>, or email <a href=\"mailto:hello@saasquatchlab.com\">hello@saasquatchlab.com</a>.",
                "EU/EEA and UK users have GDPR rights including restriction, objection, and portability. California residents have CCPA/CPRA rights — and we do not sell or share personal information as those terms are defined."]),
            ("Children", ["Sasquatch Social is not intended for anyone under 13, and we do not knowingly collect their information."]),
            ("Security", ["Traffic is encrypted with TLS. Data is held in access-controlled managed infrastructure with row-level authorisation, so accounts cannot reach each other&rsquo;s private data. Passwords are stored hashed."]),
        ]),
    "squatch-aphantasia": dict(
        name="Squatch Aphantasia", accent="#4f86c6", effective="10 September 2026", platforms="iOS and iPadOS only, for now.",
        short=("Squatch Aphantasia has no account and no ads. Only the material you choose to have "
               "explained ever leaves your device, and only to generate that explanation."),
        sections=[
            ("What we collect", [
                "<strong>No account.</strong> Squatch Aphantasia does not ask you to sign up or sign in, and has no user accounts of any kind.",
                "The app runs no analytics, includes no advertising SDK, and uses no advertising or tracking identifiers. Nothing about your use of the app is sold."]),
            ("What stays on the device", [
                "Your lessons, Learning Boards, quiz results, and conversations with the Ask Squatch tutor are stored only on your device.",
                "Camera, photo, and PDF text extraction happen <strong>on the device</strong>, using Apple&rsquo;s Vision framework. Once text is extracted, the source image is deleted &mdash; unless you turn on &ldquo;keep original images&rdquo; in Settings, in which case it stays on your device like everything else."]),
            ("What leaves the device, and why", [
                "The only data that ever leaves your device is what you choose to have explained: the text you selected, a bounded summary of that lesson (its title, key facts, and Learning Board items), and the learning preferences you set during onboarding (grade level and explanation preferences). We never send a name or contact details, because we do not collect them.",
                "That data travels over HTTPS to SaaSquatch Lab&rsquo;s gateway, which forwards it to our AI provider, OpenAI, to generate the explanation, the tutor&rsquo;s reply, a quiz, or the illustration that appears with an explanation. <strong>Nothing is sent when you are simply viewing a lesson you already saved.</strong>"]),
            ("Our gateway and OpenAI", [
                "Our gateway logs only the operation type, how long it took, and whether it succeeded &mdash; never the content of what was sent.",
                "OpenAI may retain API requests for up to 30 days to monitor for abuse, under its API terms, and does not use API data to train its models. The generated illustration is returned to your device and is not kept by our gateway."]),
            ("The onboarding question about imagery", [
                "During onboarding you are asked an optional question about how you experience mental imagery. This is <strong>not a medical assessment</strong> &mdash; it only tunes how explanations are written &mdash; and the answer stays on your device."]),
            ("Not a diagnosis or treatment", ["Squatch Aphantasia is an educational accessibility tool. It does not diagnose aphantasia or any other condition, and it is not a substitute for evaluation by a medical or educational professional."]),
            ("Platforms", ["Squatch Aphantasia is available on iOS and iPadOS only, for now."]),
            ("What we never do", ["We do not sell data, share it with data brokers, or use it for advertising. We do not run an advertising SDK or use tracking identifiers. We have no account system, so we have no way to know who you are."]),
            ("Children", ["Squatch Aphantasia is built for students 13 and up and is not directed to children under 13. The app has no accounts, so it has no way to knowingly collect information from anyone, including children."]),
            ("Your rights", ["Because lessons, Learning Boards, quizzes, and tutor conversations live only on your device, deleting the app removes them completely; we hold no copy to access, correct, or delete on our end. If you have questions, email <a href=\"mailto:hello@saasquatchlab.com\">hello@saasquatchlab.com</a>."]),
        ]),
    "app-tracker": dict(
        name="App Tracker", accent="#3a6478",
        short=("App Tracker stores the applications and documents you create so they sync across "
               "your devices. Your job search is never shared with employers or recruiters."),
        sections=[
            ("What we collect", [
                "<strong>Account information</strong> — your email address and a hashed password.",
                "<strong>What you create</strong> — job applications and their status, resume versions in your vault, cover letters, notes, interview prep, and the consistency ledger recording which materials went to which employer.",
                "<strong>Imports</strong> — if you import a LinkedIn export, we process that file to populate your history."]),
            ("The consistency ledger", ["The ledger is append-only by design: it exists so you can prove to yourself what you told an employer and when. It is private to your account. We do not surface it to employers and there is no mechanism by which an employer could request it from us."]),
            ("AI writing features", [
                "When you use an AI feature, the text you submit — the posting, your resume content, your prompt — is sent to our AI provider to generate the requested document.",
                "<strong>That content is not used to train third-party models</strong>, and it is not shared beyond generating your result."]),
            ("What we never do", ["We never share your job search with employers, recruiters, or data brokers. We do not tell your current employer you are looking. We do not sell your information."]),
            ("Payments", ["Pro subscriptions are billed through Stripe on the web. <strong>We never see or store your card number.</strong>"]),
            ("Retention", ["Your data is kept while your account is open and deleted within 30 days of account deletion, except where law requires retention."]),
            ("Your rights", ["You can access, correct, export, or delete your data — email <a href=\"mailto:hello@saasquatchlab.com\">hello@saasquatchlab.com</a>. GDPR and CCPA/CPRA rights apply as described in our <a href=\"/privacy#rights\">company privacy policy</a>. We do not sell or share personal information."]),
            ("Security", ["TLS in transit, access-controlled managed infrastructure with row-level authorisation, hashed passwords, and resume files held in an access-controlled store."]),
        ]),
}
