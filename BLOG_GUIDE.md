# Swastha Blog Publishing Guide

## Workflow

1. **Research** — Search for current food/catering industry trends in Serbia and globally
2. **Propose** — Present 2-3 topic ideas with brief rationale to user for approval
3. **Write** — After approval, generate the full blog post
4. **Publish** — Add the post to the site (steps below)

## Publishing Steps

1. Copy `blog-post.html` and rename it (e.g. `blog-mediteranska-ishrana.html`)
2. Update in the new file:
   - `<title>` tag
   - Meta description and keywords
   - OG tags (title, description, image, url)
   - Schema.org BlogPosting data (headline, description, datePublished, image)
   - Canonical URL
   - Article hero image
   - Category badge
   - Date
   - Reading time
   - Article title (h1)
   - Full article body (both EN and SR translations in the JS translations object)
   - Article tags
   - Related posts (update to link to other real posts)
3. Add a new card in `blog.html`:
   - Add `<article class="blog-card">` block in the `#blogGrid`
   - Set correct `data-category`, image, date, title, excerpt, link
   - Update SR translations in `blog.html` JS for new post keys
4. Update `sitemap.xml` — add new `<url>` entry with correct loc and lastmod
5. Git commit and push

## Content Rules

- **NO em dashes** — never use the em dash character anywhere in blog content
- Use commas, periods, colons, or rephrase instead
- Write in a professional but approachable tone
- Include relevant SEO keywords naturally (ketering, zdrava ishrana, corporate catering, etc.)
- Each post should be 800-1200 words
- Include at least one inline image
- Always provide full Serbian translation in the JS translations object

## Categories

- `healthy-eating` — Zdrava Ishrana
- `corporate-catering` — Korporativni Ketering
- `food-trends` — Food Trendovi
- `wellness` — Velnes

## SEO Keywords to Target

### Serbian
ketering beograd, ketering za firme, korporativni ketering, zdrava ishrana,
poslovni ručak, premium ketering, ketering dostava, ketering cene,
zdravi obroci za firme, dostava hrane za firme, dnevni obroci za zaposlene

### English
catering belgrade, corporate catering serbia, healthy catering,
office lunch catering, corporate meal delivery, event catering belgrade,
workplace wellness nutrition, healthy meal delivery belgrade
