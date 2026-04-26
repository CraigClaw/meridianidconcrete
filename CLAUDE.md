# Meridian Concrete Solutions — Rank & Rent Website

## Project Overview
Local lead generation website for concrete services in Meridian/Boise, Idaho. The site ranks on Google for local concrete searches, then gets rented to a local concrete contractor for $500-1000/month.

## Target Domain
meridianidconcrete.com

## Business Info (EXACT — use on every page)
- Business Name: Meridian Concrete Solutions
- Phone: (208) 555-0147 (placeholder tracking number)
- Address: 123 E Fairview Ave, Meridian, ID 83642 (placeholder)
- Hours: Mon-Sat 7:00 AM - 6:00 PM
- Service Area: Boise, Meridian, Eagle, Star, Kuna, Nampa, Caldwell, Middleton — Treasure Valley, Idaho
- Email: info@meridianidconcrete.com

---

## DESIGN SYSTEM — Warm Terracotta Editorial

This site uses a warm editorial aesthetic. NOT corporate blue, NOT generic contractor. Think: a well-designed magazine spread for a trusted local craftsman.

### Color Palette
```
--bg-primary:      #f4f3ee   /* cream, page background */
--bg-secondary:    #eeede6   /* subtle surface lift, cards */
--bg-inverse:      #191817   /* near-black, footer + CTA sections */
--text-primary:    #191817   /* ink, body text */
--text-secondary:  #4d4a43   /* warm gray, descriptions — WCAG AA on cream */
--text-muted:      #6f695f   /* subtle text, captions — WCAG AA on cream/white */
--accent:          #b15335   /* terracotta — PRIMARY ACTION COLOR, WCAG AA with cream text */
--accent-hover:    #964530   /* darker terracotta on hover, WCAG AA with cream text */
--accent-soft:     #e89268   /* soft terracotta, callouts */
--border:          #d8d3c8   /* warm border */
--success:         #5a6a32   /* olive green, verified badges — WCAG AA */
--warning:         #7a6b2e   /* amber — WCAG AA */
--danger:          #a53e2a   /* red */
--surface:         #ffffff   /* white cards on cream bg */
```

### Rules
- ONE accent (terracotta) per viewport. Never competes with itself.
- No purple gradients. No blue corporate. No neon glows.
- Flat by default — no drop shadows. Depth from surface color shifts and 1px borders only.
- Exception: modals can use `0 8px 24px rgba(25, 24, 23, 0.08)`.
- Background is cream (#f4f3ee), NOT white. White only for card surfaces.

### Typography
- **Display/Headlines:** serif — `Playfair Display`, `Georgia`, serif. Weight 700.
- **Body:** humanist sans — `Inter`, `-apple-system`, sans-serif. Weight 400. Line-height 1.65.
- **UI/Labels:** Inter, weight 600, letter-spacing +2%, uppercase for eyebrow labels only.
- **Phone CTA:** Inter, weight 700, large (24px+), terracotta color.
- Type scale: 14 / 16 / 18 / 21 / 26 / 32 / 40 / 52 / 64.
- Headlines: `text-wrap: balance`. Body: `text-wrap: pretty`.

### Components
- **Primary Button:** terracotta fill (#c96442), cream text, radius 6px, padding 12px 24px, weight 600. Hover: #b55738, no lift/scale.
- **Secondary Button:** 1px border var(--border), ink text, transparent fill. Hover: bg-secondary.
- **Ghost Link:** ink text, terracotta underline on hover.
- **Cards:** bg-secondary, no border by default, radius 8px, padding 24px. Hover: border appears.
- **Inputs:** 1px border, radius 6px, padding 10px 14px. Focus: 2px terracotta outline with 2px offset.
- **Navigation:** horizontal, underline-on-hover, terracotta underline on active. No pill backgrounds.

### Layout
- Max content: 680px (long-form), 1200px (full pages).
- 12-column grid, 24px gutters.
- Vertical rhythm: 8px baseline. Section breaks = 80-96px.
- Prominent phone number in header — click-to-call on mobile.
- Sticky mobile CTA bar with phone number.

### Do's
- Let whitespace do the heavy lifting
- Serif headlines, sans body
- Typographic hierarchy before color
- Full sentences for microcopy with periods
- Terracotta for CTAs and key emphasis only

### Don'ts
- NO purple/green/blue gradients
- NO Inter on every surface (serifs for headlines!)
- NO scale/lift animations on hover
- NO emojis in UI
- NO generic "hero + 3-col features + CTA" layout without personality
- NO Lorem ipsum, NO "coming soon"

---

## SEO Requirements (use toprank skill when available)
Every page MUST have:
1. Schema markup: LocalBusiness, Service, FAQPage, BreadcrumbList
2. Meta title (55-60 chars) and description (150-155 chars) with target keywords
3. H1 with primary keyword, H2s with secondary keywords
4. Internal links to all service pages and top location pages
5. NAP (Name, Address, Phone) in footer on every page
6. Alt text on all images with descriptive keywords
7. Canonical URLs (https://meridianidconcrete.com/...)
8. Open Graph + Twitter Card meta tags
9. Proper heading hierarchy (single H1, logical H2/H3 flow)
10. Mobile-first responsive design
11. Fast loading — inline critical CSS, no external JS frameworks, lazy-load images
12. Sitemap.xml and robots.txt

## Target Keywords
- Primary: concrete contractor meridian id, concrete contractor boise id, meridian concrete company
- Secondary: concrete driveway meridian, concrete patio boise, stamped concrete boise idaho
- Long-tail: how much does a concrete driveway cost in boise idaho

## Site Structure — Build ALL Pages
1. index.html — Homepage: hero with phone CTA, services grid, testimonials, FAQ schema, CTA banner
2. concrete-driveways.html — Driveways: types, costs, HowTo schema, local refs
3. concrete-patios.html — Patios: design options, stamped patterns, Idaho climate tips
4. stamped-concrete.html — Stamped concrete: patterns, colors, cost vs stone
5. concrete-repair.html — Repair: freeze-thaw damage, crack repair, resurfacing
6. concrete-sidewalks.html — Sidewalks: residential/commercial, ADA compliance
7. foundations-slabs.html — Foundations & slabs: new construction, garages
8. retaining-walls.html — Retaining walls: decorative + functional, Idaho soil
9. about.html — Company story, values, community involvement
10. contact.html — Contact form, map embed, NAP, service area
11. blog.html — Blog listing
12. blog-concrete-vs-asphalt.html, blog-driveway-replacement.html, blog-patio-finishes.html
13. boise-id.html, meridian-id.html, eagle-id.html, kuna-id.html, nampa-id.html, star-id.html — Location pages (each UNIQUE content, local landmarks, neighborhoods, zip codes)
14. privacy.html, terms.html — Legal pages
15. 404.html

## Technical Requirements
- Pure HTML/CSS/JS — NO frameworks, NO build step
- Google Fonts: Playfair Display (serif headlines) + Inter (sans body)
- Inline SVG icons, no icon libraries
- Semantic HTML5 markup
- WCAG 2.1 AA accessible (contrast, alt text, ARIA, focus states)
- Lazy-load below-fold images
- Print stylesheet basic support
- 90+ Lighthouse SEO + Performance target

## CRITICAL RULES
- Every page: 500+ words of unique, E-E-A-T content referencing Idaho/Treasure Valley specifics
- Location pages: each one UNIQUE — different landmarks, neighborhoods, zip codes, testimonials
- Phone number visible in header on every page
- Schema markup with LocalBusiness + geo-coordinates on every page
- All pages internally linked
- Homepage links to ALL service pages + top location pages
- Content references Idaho climate (freeze-thaw), soil conditions, local areas
- NO lorem ipsum, NO placeholder text, NO "coming soon"