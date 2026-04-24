# ronnelestrada.com

Personal brand website for **Ronnel Estrada** — licensed real estate advisor and clean energy consultant based in Cebu City, Philippines.

**Live site:** [ronnelestrada.com](https://ronnelestrada.com)

---

## What's in this repo

```
├── index.html          # The entire site (HTML + CSS + JS in one file)
├── 404.html            # Branded "lost at sea" fallback page
├── CNAME               # Custom domain binding for GitHub Pages
├── .nojekyll           # Tells GitHub Pages not to run Jekyll processing
├── robots.txt          # Tells search engines how to crawl the site
├── sitemap.xml         # SEO sitemap
├── make_og.py          # Python script to regenerate the OG image
└── assets/
    ├── ronnel-hero.png     # Hero section portrait (Cebu indoor)
    ├── ronnel-siargao.png  # Story section (Siargao sunset)
    ├── ronnel-cebu.png     # Cebu feature section (rooftop)
    └── og-image.png        # 1200x630 Open Graph social share image
```

---

## Deploy to GitHub Pages — first time

### Step 1 — Create the repo
If you don't already have one:

1. Go to [github.com/new](https://github.com/new)
2. Name the repo: `ronnelestrada.com` (or whatever you prefer — it doesn't have to match the domain)
3. Set it to **Public** (required for free GitHub Pages)
4. Skip README/gitignore/license checkboxes — we have our own files
5. Click **Create repository**

### Step 2 — Push this folder to GitHub
From inside this folder, in your terminal:

```bash
git init
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ronnelestrada.com.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

### Step 3 — Enable GitHub Pages
1. In your repo on GitHub, go to **Settings** → **Pages** (left sidebar)
2. Under "Source", pick **Deploy from a branch**
3. Branch: **main** · Folder: **/ (root)**
4. Click **Save**
5. Wait 1–2 minutes for the first build

GitHub will give you a URL like `https://YOUR-USERNAME.github.io/ronnelestrada.com` — the site is live there immediately.

### Step 4 — Connect the custom domain (ronnelestrada.com)
The `CNAME` file in this repo already tells GitHub your domain. You just need to point the domain to GitHub.

**In your domain registrar's DNS panel** (Namecheap, GoDaddy, Cloudflare, etc.) — add these records:

| Type | Host | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | YOUR-USERNAME.github.io |

Then back in **GitHub → Settings → Pages**:
1. In the "Custom domain" field, type `ronnelestrada.com` and click **Save**
2. Wait for DNS to propagate (usually 5–60 minutes)
3. Once verified, check the **Enforce HTTPS** box

That's it. `https://ronnelestrada.com` will serve this site.

---

## Making updates

### Edit text or layout
Open `index.html` — the entire site lives in this one file (HTML, CSS, and JavaScript are all inside). Edit, save, commit, push:

```bash
git add .
git commit -m "Update hero copy"
git push
```

GitHub Pages auto-rebuilds in 30–60 seconds.

### Swap a photo
Drop the new photo in `assets/` using the same filename (e.g. replace `ronnel-hero.png`). Commit and push. If you use a different filename, update the `<img src="...">` reference inside `index.html`.

### Regenerate the OG image
The OG image (`assets/og-image.png`) is the preview that shows when the site is shared on Facebook, LinkedIn, X, etc. To regenerate it with new photos or copy:

```bash
python make_og.py
```

This produces a fresh 1200×630 PNG. Commit and push.

Test how it renders on social:
- Facebook: [developers.facebook.com/tools/debug](https://developers.facebook.com/tools/debug/)
- LinkedIn: [linkedin.com/post-inspector](https://www.linkedin.com/post-inspector/)
- X/Twitter: [cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator) (or just paste the URL into a test tweet)

After any update to the OG image, use the Facebook debugger above and click "Scrape Again" to force a refresh of the cached preview.

---

## Connecting the email form

The "OFW Condo Checklist" lead magnet form currently shows a placeholder alert. To activate it:

**Option A — ConvertKit (recommended for personal brands)**
1. Create a free account at [convertkit.com](https://convertkit.com)
2. Create a form → grab the embed HTML
3. Replace the `<form class="lead-form">…</form>` block in `index.html` with the embed code

**Option B — MailerLite, Mailchimp, Kit, or Substack**
Same flow. Any email platform will give you an embed snippet. Paste it in place of the form.

**Option C — Netlify Forms (if you ever switch from GitHub Pages to Netlify)**
Add `netlify` to the `<form>` tag: `<form class="lead-form" netlify>` and Netlify handles submissions automatically.

---

## Local preview

To view the site locally before pushing changes:

```bash
cd /path/to/this/folder
python -m http.server 8000
```

Open `http://localhost:8000` in your browser.

---

## Tech stack

- **HTML/CSS/JS** — vanilla, no build step, no frameworks
- **Fonts** — Fraunces (display) + Inter (body), loaded from Google Fonts
- **Hosting** — GitHub Pages (free, fast, HTTPS)
- **Domain** — ronnelestrada.com

The site is a single static file with no dependencies. It loads fast, works without JavaScript (progressive enhancement for scroll reveal and nav shade), and scores high on Lighthouse performance out of the box.

---

## License

All content, photography, and writing on this site are © Ronnel Estrada. Code structure is provided as-is for personal reference.
