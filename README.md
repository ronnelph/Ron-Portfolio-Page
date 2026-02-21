# Ronnel Estrada — Personal Landing Page

A personal landing page showcasing my story, expertise, passions, and contact information.

## 🚀 Deployment (GitHub Pages)

1. Create a new repository on GitHub (e.g., `ronnelestrada.github.io` for a user site, or any name for a project site)
2. Push this folder to the `main` branch
3. Go to **Settings → Pages → Source** and select `main` branch
4. Your site will be live at `https://<username>.github.io/` or `https://<username>.github.io/<repo-name>/`

### Custom Domain (optional)
To use `ronnelestrada.com`:
1. In **Settings → Pages**, enter your custom domain
2. Add the following DNS records with your domain registrar:
   - `A` records pointing to GitHub Pages IPs (see [GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site))
   - `CNAME` record: `www` → `<username>.github.io`

## 📁 Structure

```
├── index.html          # Main landing page (single file, no build step)
├── assets/
│   └── ronnel-photo.jpg  # Professional headshot
└── README.md
```

## 🎨 Tech Stack

- Pure HTML, CSS, and vanilla JavaScript — no frameworks, no build tools
- Google Fonts (Playfair Display + Source Sans 3)
- Scroll-reveal animations via Intersection Observer API
- Fully responsive (mobile, tablet, desktop)

## 📝 License

© 2026 Ronnel Estrada. All rights reserved.
