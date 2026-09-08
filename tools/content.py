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
        category="Fitness &middot; iOS",
        tagline="Log the set. Close the phone.",
        blurb=("A no-nonsense workout tracker built for the gym floor. Log lifts in seconds "
               "between sets, watch strength trend upward, and keep every rep on your device — "
               "your training data never touches a server."),
        meta=["130+ exercise library", "Personal record tracking", "Zero networking", "iPhone &amp; iPad"],
        hero_note="Three full workouts free &middot; Pro $4.99/month or $29.99/year &middot; No account, ever",
        ctas=[("Coming to the App Store", "#", "primary", False)],
        promise=("Squatch Lift has <strong>no servers and makes no network requests at all</strong>. "
                 "Your workouts, measurements, and photos live in a database on your phone. "
                 "We could not see your training data if we wanted to."),
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
            ("Android", ["Squatch Lift is iPhone and iPad only today. An Android version is planned but not yet in development — we would rather ship one good platform than two rushed ones."])],
    ),
    dict(
        slug="sizesquatch", name="SizeSquatch", accent="#a5dcc0",
        logo="logo-sizesquatch.png", tag="Live", tagclass="live",
        category="Photo utility &middot; iOS",
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
        short="Squatch Lift collects nothing. It has no servers and makes no network requests.",
        sections=[
            ("What we collect", ["<strong>Nothing.</strong> Squatch Lift has no backend, no user accounts, no analytics, no advertising SDKs, and no third-party trackers. The app makes no network connections of its own."]),
            ("Your training data", [
                "Your workouts, exercise history, personal records, body measurements, supplement log, custom exercises, and templates are stored in a database <strong>on your device</strong> using Apple&rsquo;s on-device storage framework.",
                "This data is never transmitted to us or to anyone else. We have no copy of it and no way to obtain one. If you delete the app, the data is deleted with it, so keep a device backup if you want to preserve your history."]),
            ("Photos", ["If you attach a selfie to a workout share card, the image is used only to render that card on your device. It is not uploaded. Where the resulting card goes afterwards is entirely your choice."]),
            ("Health data", ["Squatch Lift does not read from or write to Apple Health. The measurements you enter are typed by you and stay in the app."]),
            ("Subscriptions", [
                "Squatch Lift Pro is an auto-renewing subscription ($4.99/month or $29.99/year) sold through Apple. <strong>Apple processes the payment; we never receive your card details or your Apple Account identity.</strong> The app receives only a signed receipt confirming whether a subscription is active, and it validates that on your device.",
                "Manage or cancel from your App Store account settings. Full terms are in our <a href=\"/terms#subscriptions\">Terms of Use</a>."]),
            ("What we never do", ["We do not sell data, share it with data brokers, or use it for advertising — a claim that is easy for us to make, because the data never leaves your phone."]),
            ("Children", ["Squatch Lift is not directed to children under 13 and collects no personal information from anyone."]),
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
