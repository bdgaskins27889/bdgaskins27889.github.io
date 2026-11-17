# BMN Newsroom 2.0 — development only

Branch: `bmn-newsroom-v2`. Production remains on `main` until reviewed and merged.

## Preserved
- `bmn/index.html`: original BMN homepage
- `bmn/verify-BMN-001.html`: organization-issued credential verification
- Existing assets, press dossier, editorial policy and unrelated portfolio content

## Added
- `bmn/news/index.html`: newsroom archive landing page
- `bmn/news/article-template.html`: noindex editorial article template
- `bmn/assets/newsroom.css`: shared responsive newsroom styles

## Before launch
1. Review logo, navigation, accessibility and mobile layout.
2. Confirm existing pages and internal links work.
3. Add original fact-checked articles only after editorial approval.
4. Create article-specific metadata, canonical URLs, Open Graph images and NewsArticle structured data for actual articles.
5. Generate sitemap.xml and robots.txt after URLs are finalized; submit sitemap to Search Console.
6. Keep private tips, unpublished records and source identifiers out of public GitHub.
7. Confirm domain ownership and configure GitHub Pages DNS and custom domain later. Update canonical URLs and arrange redirects where possible.

Do not treat this branch as a private storage location: the repository is public.
