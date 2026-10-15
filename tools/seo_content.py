"""Copy for the SEO/GEO marketing pages: Squatch Connect eSIM destination pages,
the eSIM guide, the Airalo comparison, the Squatch Lift comparison, and the App
Tracker template/comparison pages.

Kept separate from content.py (which drives the core product pages) because this
content is generated from the catalog snapshot in tools/data/connect_catalog.json
rather than hand-authored per product. See tools/data/refresh_catalog.py to update
the snapshot.

Every fact here is one of:
  - pulled from tools/data/connect_catalog.json at build time, or
  - copied from the existing /squatch-connect product page and content.py, or
  - copied from the existing /squatch-lift and /app-tracker entries in content.py.
Nothing about pricing, coverage, or competitors is invented.
"""

# Destination slugs to build. Ids match the catalog's destinationID field, except "uk"
# (catalog already uses "uk"). Order: the original 20 first (unchanged, so existing URLs
# keep their position), then every other destination in the catalog that has plans,
# alphabetically. Regenerate this list from tools/data/connect_catalog.json whenever the
# catalog is refreshed — see tools/data/refresh_catalog.py.
DESTINATION_SLUGS = [
    "mexico", "japan", "uk", "france", "italy", "spain", "canada", "germany",
    "portugal", "greece", "thailand", "south-korea", "turkey", "iceland",
    "ireland", "netherlands", "costa-rica", "dominican-republic", "colombia",
    "europe",
    "africa", "argentina", "asia", "australia", "austria", "bahrain", "bangladesh",
    "belgium", "brazil", "bulgaria", "cambodia", "chile", "china-mainland", "croatia",
    "cyprus", "czech-republic", "denmark", "ecuador", "egypt", "fiji", "finland",
    "global", "hong-kong-china", "hungary", "india", "indonesia", "israel", "jamaica",
    "jordan", "kenya", "kuwait", "laos", "luxembourg", "macao-china", "malaysia",
    "maldives", "malta", "middle-east", "morocco", "nepal", "new-zealand",
    "north-america", "norway", "oceania", "oman", "panama", "peru", "philippines",
    "poland", "qatar", "romania", "saudi-arabia", "serbia", "singapore", "slovakia",
    "slovenia", "south-africa", "south-america", "sri-lanka", "sweden", "switzerland",
    "tanzania", "tunisia", "uae", "usa", "vietnam",
]

APPSTORE_ID = "6808746597"


def appstore_url(slug):
    return "https://apps.apple.com/app/apple-store/id%s?pt=128775609&ct=seo_%s&mt=8" % (APPSTORE_ID, slug)


def play_url(slug):
    return ("https://play.google.com/store/apps/details?id=com.saasquatchlabs.squatchconnect"
            "&referrer=utm_source%%3Dsaasquatchlab%%26utm_medium%%3Dseo%%26utm_campaign%%3Dseo_%s" % slug)


def faqs_for(name, is_region):
    """FAQ Q&A grounded only in facts already published on /squatch-connect."""
    where = "in %s" % name if is_region else "for %s" % name
    qas = [
        ("Do I need an account to buy an eSIM %s?" % where,
         "No. Squatch Connect has no user accounts at all — you pick a destination and a plan, pay as a "
         "guest with Apple Pay or a card through Stripe, and the eSIM is ready to install. We process the "
         "destination you picked and an email for your receipt; Stripe handles the payment and we never see "
         "your card."),
        ("How do I install the eSIM on my iPhone?",
         "On iOS 17.4 and later, Squatch Connect installs the eSIM through Apple's own provisioning link in "
         "one tap — no QR code needed. A QR code and manual entry are always available as fallbacks if your "
         "device or iOS version doesn't support the one-tap flow. You can also say &ldquo;Hey Siri, add an "
         "eSIM for %s in Squatch Connect&rdquo; and let the App Shortcut do it." % name),
        ("Will my phone work with this eSIM?",
         "Your phone needs to be unlocked and eSIM-capable. Squatch Connect warns you before purchase if your "
         "device may be carrier-locked, because an eSIM you can't install isn't a bargain — check that warning "
         "before you buy."),
        ("Can I tether or use a mobile hotspot on this plan?",
         "Every plan we list permits tethering. Larger plans are also flagged as hotspot-ready tiers for "
         "heavier use, like getting a laptop online too."),
        ("What happens when my data runs out?",
         "Squatch Connect is pay-as-you-travel, not a subscription — there's no auto-renewal to worry about. "
         "A live gauge in the app shows exactly how much data is left and when the plan expires, refreshed "
         "when you open the app or pull to refresh, and you can simply buy another plan when you need one."),
        ("Does this eSIM encrypt or anonymize my traffic like a VPN?",
         "No — Squatch Connect is a connectivity product, not a privacy tunnel. It gets you working mobile "
         "data at local rates instead of your carrier's roaming price, but it doesn't encrypt or anonymize "
         "your traffic beyond what normal cellular service already does. We'd rather say that plainly than "
         "let you assume otherwise."),
    ]
    return qas


HOW_IT_WORKS = {
    "iphone": [
        "Download Squatch Connect, pick your destination and a plan, and pay as a guest with Apple Pay or a "
        "card — no account to create.",
        "On iOS 17.4 and later, tap install and the eSIM provisions through Apple's own setup link in one "
        "step. On earlier versions, scan the QR code Squatch Connect shows you, or enter the details "
        "manually in Settings &rsaquo; Cellular &rsaquo; Add eSIM.",
        "Your phone needs to be unlocked and eSIM-capable — the app checks and warns you before you pay if "
        "your device may be carrier-locked.",
    ],
    "android": [
        "Squatch Connect's Android build carries the same destination catalog and install flow as iPhone, "
        "and is currently in internal testing on Google Play.",
        "Install by scanning the QR code Squatch Connect provides, or by entering the activation details "
        "manually in your phone's eSIM settings — the exact menu wording varies by manufacturer.",
        "As with iPhone, your Android phone needs to be unlocked and eSIM-capable for this to work.",
    ],
}


GUIDE_SECTIONS = [
    ("Check your phone is eSIM-capable and unlocked",
     ["An eSIM is a digital SIM built into your phone instead of a physical card you swap in — but it only "
      "works if two things are true: your phone model supports eSIM, and your phone is unlocked from your "
      "current carrier.",
      "Most iPhones from the XS/XR generation onward, and most recent flagship Android phones, support eSIM. "
      "A phone bought on an installment plan or carrier contract is sometimes locked even if it's eSIM-capable "
      "— check with your carrier if you're not sure, since a locked phone can't add a second carrier's eSIM."]),
    ("Install the eSIM before you fly",
     ["Install your travel eSIM while you still have Wi-Fi or your home data connection — arriving and "
      "discovering you need connectivity to set up connectivity is the exact problem an eSIM is supposed to "
      "solve.",
      "On iPhones running iOS 17.4 or later, Squatch Connect can install the eSIM in one tap through Apple's "
      "own provisioning link. Older iOS versions, and most Android phones, install via a QR code the app "
      "shows you, or by entering the activation details manually in your phone's cellular settings."]),
    ("Turn on data roaming for the eSIM line only",
     ["Installing the eSIM adds it as a second line — it doesn't activate on its own. Go into your phone's "
      "cellular or SIM settings, select the new eSIM line, and turn on data roaming for that line specifically.",
      "This is also the point to set your eSIM as the line used for cellular data (while keeping your home "
      "SIM as the default for calls and texts, see below) so your phone actually uses the local data plan "
      "instead of racking up roaming charges on your home carrier."]),
    ("Keep your home SIM active for calls and texts",
     ["You don't need to remove or disable your home SIM to use a travel eSIM — most phones run both at once. "
      "Keep your physical SIM or home eSIM active for calls and texts on your usual number, and let the new "
      "travel eSIM carry the data.",
      "This is exactly the setup Squatch Connect is built around: a second data-only line you add for a trip "
      "and can leave installed for the next one, without touching your primary number."]),
]


AIRALO_ALT_INTRO = (
    "If you're comparing travel eSIM apps, here's what we can tell you honestly about Squatch Connect versus "
    "the alternatives — without putting words in a competitor's mouth."
)

AIRALO_ALT_SQUATCH_FACTS = [
    ("No account required", "Squatch Connect has no user accounts at all. You pick a destination, pick a "
     "plan, and check out as a guest with Apple Pay or a card through Stripe. We process the destination "
     "you picked and an email for your receipt — nothing else."),
    ("Price per GB shown upfront", "Every plan in the app and on these destination pages lists the exact "
     "price alongside the data allowance, so the effective price per gigabyte is a glance away rather than a "
     "spreadsheet exercise."),
    ("One-tap install on newer iPhones", "On iOS 17.4 and later, the eSIM installs through Apple's own "
     "provisioning link in a single tap, with QR and manual entry available as fallbacks."),
    ("Pay-as-you-travel, no subscription", "Plans are one-time purchases sized for a trip — there is no "
     "recurring subscription to remember to cancel."),
    ("Ask Siri", "App Shortcuts let you add an eSIM for a destination by voice on iOS, without opening the "
     "app."),
]

AIRALO_ALT_HOW_TO_COMPARE = [
    "Whichever eSIM app you're evaluating, the same handful of questions get you a real comparison: Does it "
    "require an account, and what does that account collect? Is the price per gigabyte shown before you buy, "
    "or do you have to do the division yourself? Is checkout guest-friendly, or does it push you through a "
    "sign-up wall? Does the plan expire on a subscription cycle, or is it a one-time purchase sized for your "
    "trip?",
    "We're not going to quote another provider's prices or policies here without pulling them from a source "
    "we can point to — pricing and account requirements change, and a stale claim about a competitor helps "
    "no one. Compare the plan for your actual destination on each app's own site, using the questions above.",
]


NO_ACCOUNT_INTRO = (
    "Squatch Connect has no sign-up screen, no login, and no password. That is a real feature, not a "
    "marketing word — here is precisely what it means, and precisely what we still process, so you're not "
    "guessing."
)

NO_ACCOUNT_HOW = [
    ("No account to create", "There is no sign-up form anywhere in Squatch Connect. You open the app, pick "
     "a destination, pick a plan, and check out. No username, no password, nothing to remember for next "
     "trip."),
    ("Guest checkout only", "Checkout runs as a guest, through Apple Pay or a card, processed by Stripe. "
     "Squatch Connect never sees or stores your card number, and does not keep cards on file."),
    ("No passport or ID upload", "We do not ask for a passport scan or any identity document before selling "
     "a plan. Travel eSIMs are roaming data products registered in their issuing country, not financial or "
     "government services that require that kind of check."),
]

NO_ACCOUNT_NOT_ANONYMOUS = (
    "One thing we want to say plainly: this is not anonymous. Paying by card or Apple Pay identifies you to "
    "your card network, your bank, and to Stripe, the payment processor — that is simply how card payments "
    "work, on any app. What &ldquo;no account&rdquo; actually buys you is no sign-up screen, no password, and "
    "no profile Squatch Connect itself asks you to build. It does not make the purchase untraceable."
)

NO_ACCOUNT_DATA_FACTS = [
    ("The destination and plan you pick", "That's what lets us provision the right eSIM — a country or "
     "region and a data/validity tier, nothing more."),
    ("An email for your receipt", "Checkout collects an email so Stripe or Apple Pay can send a payment "
     "receipt. It's not used for marketing email."),
    ("Order id, ICCID, activation code, plan, and expiry", "The minimum needed for your eSIM to work and "
     "for support if something goes wrong. Order records are deleted 90 days after the plan expires."),
    ("A usage byte count tied to the eSIM", "We query the network supplier for how much data your eSIM has "
     "used so the app and widget can show data remaining — tied to the eSIM, not to your identity."),
    ("Nothing from your card", "Stripe handles the payment directly. Squatch Connect never sees or stores "
     "your card number."),
]

NO_ACCOUNT_FAQS = [
    ("Do I have to create an account to buy an eSIM?",
     "No. Squatch Connect has no user accounts at all — there is no sign-up screen or password anywhere in "
     "the app. You pick a destination and a plan, then check out as a guest."),
    ("Is checkout really guest checkout?",
     "Yes. You pay with Apple Pay or a card, processed by Stripe. Squatch Connect never sees or stores your "
     "card number and does not keep cards on file."),
    ("Is a no-account eSIM the same as an anonymous one?",
     "No, and we're not going to pretend otherwise. A card or Apple Pay payment identifies you to your bank, "
     "card network, and Stripe — that's true of any app's checkout, not a limitation specific to us. &ldquo;No "
     "account&rdquo; means no sign-up screen and no password with Squatch Connect itself, not that the "
     "purchase can't be traced by the payment processor."),
    ("Do you ask for a passport or ID before I can buy a plan?",
     "No. There is no passport upload or identity document check. Travel eSIMs are roaming data products "
     "registered in their issuing country, not financial or government services."),
    ("What information does Squatch Connect actually keep?",
     "The destination and plan you picked, an email for your payment receipt, an order id, your eSIM's "
     "ICCID and activation code, the plan's expiry, and a usage byte count tied to the eSIM. Order records "
     "are deleted 90 days after the plan expires. Full detail is in our <a href=\"/squatch-connect/privacy\">"
     "privacy policy</a>."),
    ("Can I delete my data afterward?",
     "Yes. Contact support@saasquatchlab.com with the order id or ICCID shown in the app to request "
     "deletion of your order records."),
]


SQUATCH_LIFT_FACTS = [
    ("On-device only, no account", "Squatch Lift has no servers of its own. Your workouts, measurements, "
     "and photos live in a database on your phone — there's no account to create and no login screen."),
    ("Free tier, then a flat subscription", "Your first three completed workouts are free with no account "
     "and no card. After that, Squatch Lift Pro is $4.99 per month or $29.99 per year, unlocking unlimited "
     "use."),
    ("130+ exercise library", "A full exercise catalogue out of the box, plus your own custom movements and "
     "templates covering standard training splits."),
    ("Personal record tracking", "Personal records surface the moment you beat them, mid-workout."),
    ("History and strength trends", "Charts showing whether recent training has actually moved a given lift, "
     "plus body measurements tracked alongside it."),
    ("Share cards", "A clean workout summary card you can render and post wherever you like — you choose "
     "what leaves the phone, since nothing leaves it automatically."),
]

SQUATCH_LIFT_COMPARE_NOTE = (
    "We know Hevy and Strong by reputation as established workout-logging apps with large communities and "
    "social features. Rather than describe their current pricing or feature set from memory — which risks "
    "being stale or simply wrong — we're laying out what we can verify about Squatch Lift, and encouraging "
    "you to check each competitor's own app listing for their current plans. The one comparison we're "
    "confident stating: Squatch Lift is built with no account and no server round-trip for your training "
    "data, which is not the default architecture for most workout trackers."
)


APP_TRACKER_FACTS = [
    ("Resume vault", "Versioned resume variants, kept properly rather than as a folder of near-identical "
     "files with dates in the filename."),
    ("Consistency ledger", "An append-only record of which resume, which claims, and which answers went to "
     "which employer, so you don't contradict yourself in round three."),
    ("Application pipeline", "Every application with its status, next step, and reminders."),
    ("AI writing suite", "Draft tailored resumes, cover letters, and thank-you notes against a specific "
     "posting, starting from what's already in your vault."),
    ("LinkedIn import", "Bring your history in from a LinkedIn export rather than retyping a decade of "
     "roles."),
    ("Pricing", "Free to start. Pro is $9 per month or $79 per year, billed through Stripe on the web."),
]

APP_TRACKER_COMPARE_NOTE = (
    "Teal and Huntr are established job-search trackers with their own feature sets and pricing, which "
    "change over time — rather than describe them from memory, we're stating what App Tracker actually does "
    "and pointing you to each competitor's own site for their current plans. The distinguishing idea behind "
    "App Tracker is the consistency ledger: an append-only record of exactly which resume version and which "
    "claims went to which employer, built for a search that runs long enough that you can no longer keep "
    "that straight in your head."
)

TEMPLATE_ROWS = [
    dict(company="", role="", date_applied="", resume_version="", contact="", status="", next_step=""),
] * 8
