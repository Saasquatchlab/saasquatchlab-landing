# saasquatchlab-landing — Agent Context

Static site for **saasquatchlab.com** (SaaSquatch Lab company landing). No build step, no framework — plain HTML/CSS served by Vercel (project `saasquatchlab-landing`, deploy with `vercel deploy --prod`).

## ⚠️ NEVER create a `public/` directory in this repo

This project has no build step, so **if a `public/` folder exists, Vercel serves ONLY that folder and the entire site 404s** (home, /support, /sizesquatch, privacy pages — everything). This took the site down for ~6 hours on 2026-09-02 when ad assets were committed under `public/ads/`.

- Static assets (images, video, ad creatives) go in **root-level folders**: `ads/`, `sizesquatch/`, etc.
- Ad assets for any product belong in `ads/<product>/` (e.g. `ads/squatchlift/`, `ads/sizesquatch-*.png`). They're served at `https://saasquatchlab.com/ads/...`.
- After ANY deploy, verify the site is up: `curl -s -o /dev/null -w "%{http_code}" -L https://saasquatchlab.com` must return 200.

## Structure

- `index.html` — landing page (product cards: Sasquatch Social, SizeSquatch, App Tracker, Sasquatch Polling)
- `sizesquatch/` — SizeSquatch product page (ad-campaign destination — Meta ads link here; do not break this URL)
- `sizesquatch/privacy/` — privacy policy (**registered with Apple's App Store** — do not move or delete)
- `support/` — support page (**registered with Apple's App Store** — do not move or delete)
- `ads/` — publicly hosted ad creatives

## Registered external references (breaking these URLs breaks other systems)

| URL | Referenced by |
|---|---|
| `/support` | App Store Connect (SizeSquatch support URL) |
| `/sizesquatch/privacy` | App Store Connect (SizeSquatch privacy policy URL) |
| `/sizesquatch` | Meta ads campaign 52596210525195 (link destination) |
| `/ads/*` | Meta ad library image sources |

Domain DNS: AWS Route 53 (zone Z0940405PC2A5NJQUM30). Apex 307-redirects to www. Email: Google Workspace (`hello@saasquatchlab.com`).
