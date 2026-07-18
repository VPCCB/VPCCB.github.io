# My Blog

A minimalist personal site with a warm **terracotta** theme, built with
[Astro](https://astro.build) and deployed free on **GitHub Pages**.

- ✍️ **Writing** — add posts as Markdown files, no code needed
- 🎨 **Terracotta theme** — edit one file to recolor the whole site
- 🚀 **Auto-deploy** — push to `main` and GitHub Pages rebuilds

## Run it locally

```bash
npm install       # once, to install dependencies
npm run dev        # start a live preview at http://localhost:4321
```

## Make it yours

| What to change | Where |
| --- | --- |
| Your name, tagline, nav, social links | `src/consts.ts` |
| Colors and fonts | `src/styles/global.css` (top of file) |
| About page text | `src/pages/about.astro` |
| Your projects | `src/pages/work.astro` |
| Blog posts | add Markdown files in `src/content/blog/` |

### Add a new post

Create a file like `src/content/blog/my-post.md`:

```markdown
---
title: 'My post title'
description: 'A one-line summary.'
pubDate: 2026-07-11
---

Write your thoughts in Markdown here.
```

Save it — the post appears automatically.

## Deploy to GitHub Pages

1. Create a GitHub repo.
   - For a site at `https://<username>.github.io`, name the repo **`<username>.github.io`** and keep `base` unset in `astro.config.mjs`.
   - For a site at `https://<username>.github.io/my-blog`, name the repo anything and set `base: '/my-blog'` in `astro.config.mjs`.
2. In `astro.config.mjs`, set `site` to your GitHub Pages URL.
3. Push this folder to the repo's `main` branch.
4. On GitHub: **Settings → Pages → Build and deployment → Source → GitHub Actions**.
5. Every push to `main` now rebuilds and publishes the site automatically.

## Commands

| Command | Action |
| --- | --- |
| `npm run dev` | Local dev server |
| `npm run build` | Build the static site into `dist/` |
| `npm run preview` | Preview the production build locally |
