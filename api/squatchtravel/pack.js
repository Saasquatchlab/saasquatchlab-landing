// GET /api/squatchtravel/pack?country=<iso2>
// Assembles a fresh Squatch Travel destination pack on request: country data
// + emergency numbers + phrasebook/health translations + LIVE exchange rate.
// Privacy: the request carries a country code and nothing else — no user
// data, no identifiers, no logging beyond the platform's defaults.

const COUNTRIES = require("./_data/countries.js");
const PHRASES = require("./_data/phrases.js");

// Live FX, cached in the function instance for 30 minutes. Source is the
// keyless open.er-api.com feed (rates per USD, refreshed daily upstream).
let ratesCache = { at: 0, rates: null, date: null };
async function getRates() {
  const now = Date.now();
  if (ratesCache.rates && now - ratesCache.at < 30 * 60 * 1000) return ratesCache;
  const r = await fetch("https://open.er-api.com/v6/latest/USD");
  if (!r.ok) throw new Error(`fx upstream ${r.status}`);
  const j = await r.json();
  if (j.result !== "success" || !j.rates) throw new Error("fx payload invalid");
  ratesCache = { at: now, rates: j.rates, date: (j.time_last_update_utc || "").slice(0, 16) };
  return ratesCache;
}

const GENERIC_CUSTOMS = [
  "Greetings and basic courtesy phrases in the local language go a long way — even a bad accent is appreciated.",
  "Tipping customs vary widely; check whether service is included before adding one.",
  "Dress modestly at religious sites, and ask before photographing people.",
  "Learn the local queueing and personal-space norms by watching before acting.",
];
const GENERIC_TRANSPORT = [
  "Use official taxi stands or licensed ride-hailing apps; agree on a fare or ensure the meter runs before departing.",
  "Validate public-transport tickets where machines are provided — inspectors fine on the spot in many countries.",
  "Keep small cash for buses and rural transport; cards aren't accepted everywhere.",
];
function genericSafety(name) {
  return [
    `Save the local emergency numbers for ${name} to your phone contacts before you land — this pack lists them, but verify locally on arrival.`,
    "Pickpocketing near tourist landmarks and on crowded transport is the most common risk anywhere. Keep valuables zipped and in front pockets.",
    "Photograph your passport and keep the copy separate from the original. Note your embassy's address and phone number.",
    "Use ATMs attached to banks during daylight; shield your PIN and decline 'helpful' strangers at the machine.",
    "Agree taxi fares up front or insist on the meter. Prefer licensed stands and official ride-hailing apps.",
    "Check your government's current travel advisory for this destination before departure — conditions change.",
  ];
}

module.exports = async (req, res) => {
  const code = String(req.query.country || "").toLowerCase().trim();
  if (!/^[a-z]{2}$/.test(code)) {
    return res.status(400).json({ error: "country must be an ISO-3166 alpha-2 code" });
  }
  const c = COUNTRIES[code];
  if (!c) {
    return res.status(404).json({ error: "no pack available for this country yet", country: code });
  }

  let ratePerUSD = null, rateAsOf = null;
  try {
    const { rates, date } = await getRates();
    if (rates[c.cur]) {
      ratePerUSD = Math.round(rates[c.cur] * 10000) / 10000;
      rateAsOf = date || new Date().toISOString().slice(0, 10);
    }
  } catch (e) {
    // FX unavailable: still serve the pack, marked so the client keeps any
    // fresher rate it already has.
    ratePerUSD = 0;
    rateAsOf = "unavailable";
  }

  const lang = PHRASES[c.lang] || PHRASES.en;
  const version = parseInt(new Date().toISOString().slice(0, 10).replace(/-/g, ""), 10);

  const pack = {
    id: code,
    version,
    country: c.name,
    countryCode: code.toUpperCase(),
    flag: c.flag,
    languageCode: c.lang === "arm" ? "ar" : c.lang,
    languageName: c.langName,
    currencyCode: c.cur,
    currencyName: c.curName,
    ratePerUSD,
    rateAsOf,
    usesMetric: c.metric !== false,
    timeZone: c.tz,
    coordinates: { lat: c.c[0], lon: c.c[1] },
    emergency: c.em,
    phrases: lang.phrases,
    customs: GENERIC_CUSTOMS,
    transport: GENERIC_TRANSPORT,
    safety: genericSafety(c.name),
    allergyTemplate: lang.allergyTemplate,
    medicationTemplate: lang.medicationTemplate,
    allergens: lang.allergens,
  };

  res.setHeader("Cache-Control", "s-maxage=1800, stale-while-revalidate=86400");
  res.status(200).json(pack);
};
