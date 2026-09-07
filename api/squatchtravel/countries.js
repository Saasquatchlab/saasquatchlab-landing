// GET /api/squatchtravel/countries
// Index of countries with downloadable packs: code, name, flag, language.
// Carries no user data in either direction.

const COUNTRIES = require("./_data/countries.js");
const PHRASES = require("./_data/phrases.js");

module.exports = (req, res) => {
  const list = Object.entries(COUNTRIES)
    .map(([code, c]) => ({
      code,
      name: c.name,
      flag: c.flag,
      languageName: c.langName,
      hasPhrasebook: Boolean(PHRASES[c.lang]),
    }))
    .sort((a, b) => a.name.localeCompare(b.name));
  res.setHeader("Cache-Control", "s-maxage=86400, stale-while-revalidate=604800");
  res.status(200).json({ countries: list });
};
