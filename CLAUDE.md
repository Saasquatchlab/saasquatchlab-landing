# saasquatchlab-landing — Agent Context

Static site for **saasquatchlab.com** (SaaSquatch Lab company site). Plain HTML/CSS served by Vercel (project `saasquatchlab-landing`, deploy with `vercel deploy --prod`).

**No build step at serve time.** Vercel serves the committed `.html` files directly. Pages are *generated offline* by `tools/build_site.py` and the output is committed — see below.

## ⚠️ NEVER create a `public/` directory in this repo

There is no build step, so **if a `public/` folder exists, Vercel serves ONLY that folder and the entire site 404s** (home, /support, /privacy, product pages — everything). This took the site down for ~6 hours on 2026-09-02 when ad assets were committed under `public/ads/`.

- Static assets (images, video, ad creatives) go in **root-level folders**: `ads/`, `sizesquatch/`, etc.
- Ad assets belong in `ads/<product>/` (e.g. `ads/squatchlift/`). Served at `https://saasquatchlab.com/ads/...`.
- After ANY deploy, verify: `curl -s -o /dev/null -w "%{http_code}" -L https://saasquatchlab.com` must return 200.
- `tools/build_site.py` asserts `public/` does not exist before writing anything.

## Generator

```bash
python3 tools/build_site.py      # regenerates every page listed below
```

| File | Role |
|---|---|
| `tools/build_site.py` | Design system (CSS/JS), ridgeline art, page builders |
| `tools/content.py` | Product copy, status tags, feature lists, per-app privacy policies |
| `tools/legal.py` | Hand-authored `/privacy`, `/terms`, `/support` prose |

**Edit the generator, not the generated HTML** — hand edits to generated files are lost on the next build. Product status tags (`Live` / `In App Review` / `Coming soon`) live in `content.py` and must track reality.

### Privacy copy must be per-platform, not per-app

Both shipping apps are now on **iOS and Android**, and the two platforms do not have
the same privacy story. Google Play Billing forces `INTERNET` and
`ACCESS_NETWORK_STATE` into the merged Android manifest; the iOS builds still make no
network requests at all. A blanket "makes no network requests" claim is therefore
**false on Android** — and these pages are the privacy URLs Apple *and* Google have on
file, read by reviewers against the actual manifest.

The pattern both apps now use: state the on-device guarantee unconditionally, then name
the one difference explicitly ("on Android, Google's billing library requires network
permission to process the purchase, and that is the only thing it is used for").

This bit Squatch Lift on 2026-09-08: its Play-registered `/squatch-lift/privacy` still
read "makes no network connections of its own" *while the Android build was in review
declaring three network-related permissions*. Check this whenever an app gains a
platform.

### Art direction — "It's out there"

The brand line is literal: a Pacific Northwest ridgeline at first light with the SaaSquatch mark standing in the treeline, half-occluded by the front rank of conifers. The scene is two stacked SVGs so the front trees genuinely occlude the figure. Rules the design holds to (the brief was explicitly *not* to look like a generic AI/SaaS template): asymmetric editorial grid, no pill badges, no gradient-text headlines, no boxed feature-card grids, hairline spec rows instead, tracked micro-caps for metadata, film grain + vignette for a photographic surface.

**Gotcha:** the grain layer must NOT use `mix-blend-mode`. A blended fixed full-viewport layer makes WebKit paint the whole page black on scroll. Plain low opacity looks the same on a ground this dark.

Brand marks `mark-sasquatch.png` (white silhouette, transparent) and `mark-sasquatch-dark.png` were extracted from the left figure of `logo-sasquatch-social.png` — the same sasquatch used in the app icons.

## Structure

Generated:
- `index.html` — company landing (product index, principles, about, closer)
- `sasquatch-social/`, `squatch-lift/`, `sizesquatch/`, `squatch-connect/`, `squatchtravel/`, `app-tracker/` — one landing page per product
- `sasquatch-social/privacy/`, `squatch-lift/privacy/`, `app-tracker/privacy/` — per-app privacy policies
- `privacy/`, `terms/`, `support/` — company policy, EULA, support

Hand-maintained (content already reviewed/registered — generator does not touch them):
- `sizesquatch/privacy/`, `squatch-connect/privacy/`, `squatchtravel/privacy/`

Other: `ads/` (ad creatives), `api/squatchtravel/` (Vercel functions serving Squatch Travel destination packs).

Note the inconsistent slug: Squatch Travel is `/squatchtravel` (no hyphen) because its privacy URL is already registered that way. Squatch Connect is `/squatch-connect` (hyphen). Don't "fix" either.

**Sasquatch Polling** is listed on the home index as *Coming soon* only — no product page and no privacy policy. It is not in use and is gated on Sasquatch Social reaching enough users to support credible polling.

## Registered external references (breaking these URLs breaks other systems)

| URL | Referenced by |
|---|---|
| `/support` | App Store Connect — SizeSquatch + Squatch Lift support URL |
| `/privacy` | App Store Connect — **Squatch Lift privacy policy URL**, named in its App Store description |
| `/terms` | EULA target for subscription apps |
| `/sizesquatch` | Meta ads campaign 52596210525195 (link destination — keep the App Store button above the fold) |
| `/sizesquatch/privacy` | App Store Connect — SizeSquatch privacy URL |
| `/squatch-connect/privacy` | App Store Connect — Squatch Connect privacy URL |
| `/squatchtravel/privacy` | App Store Connect — Squatch Travel privacy URL |
| `/ads/*` | Meta ad library image sources |
| `/api/squatchtravel/*` | Squatch Travel iOS app (destination packs) |
| `/sizesquatch/privacy` | **Google Play** — SizeSquatch privacy policy URL (as well as App Store) |
| `/squatch-lift/privacy` | **Google Play** — Squatch Lift privacy policy URL |
| `/support` | **Google Play** — support URL for both Android listings |

⚠️ `vercel.json` rewrites every unmatched path to `/index.html`, so a **missing page returns 200 with the landing page rather than a 404**. Broken registered URLs therefore fail silently — verify by title, not status code. `/privacy` and `/terms` were in exactly this state until 2026-09-07.

Any app shipping auto-renewable subscriptions must carry a functional Terms of Use (EULA) link in its App Store *description* — `/terms` or Apple's standard EULA. Squatch Lift was rejected under guideline 3.1.2 for omitting it.

Domain DNS: AWS Route 53 (zone Z0940405PC2A5NJQUM30). Apex 307-redirects to www. Email: Google Workspace (`hello@saasquatchlab.com`).
