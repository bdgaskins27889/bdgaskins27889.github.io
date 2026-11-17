# BMN editorial publishing workflow

This is a public repository. **Never commit confidential tips, unpublished source identifiers, protected personal data, or sensitive raw evidence.** Use private, access-controlled storage outside GitHub for source material.

## Story states
Pitch → Research → Fact-check → Legal/ethics review → Publisher approval → Publish → Monitor corrections.

## Required story metadata
- Original headline and unique slug
- Author/byline and role
- Publication date (and modification date if revised)
- Desk and article type (reporting, analysis, opinion, satire)
- Accurate summary and sources
- Source response or documented request for comment, when relevant
- Relevant conflict-of-interest disclosure
- Correction contact and update log
- Original or licensed image with credit and alt text

## SEO publishing checklist
- Copy the noindex article template to a unique, permanent filename, then remove the template warning and noindex directive **only after approval**
- Add unique title, meta description, canonical URL, Open Graph title/image/URL, and valid NewsArticle JSON-LD for actual reporting
- Use article-specific author, datePublished, dateModified, image and publisher details; never fabricate fields
- Link to relevant archive and other BMN stories; cite original primary sources
- Add only approved public URLs to bmn/sitemap.xml
- Test mobile layout, keyboard navigation, links, metadata and structured data
- Review canonical URL and sitemap when a custom domain is connected

## Backlink tracking
Log: source domain, article URL, BMN destination URL, date earned, editorial relevance, referral traffic and follow-up. Do not buy links or exchange them as a condition of coverage.

## Domain migration
Use GitHub Pages custom domain configuration when acquired. Preserve paths under /bmn/ if possible; otherwise provide redirects where supported. Update all canonicals, Open Graph URLs, structured data, sitemap and internal absolute links. Verify both hostnames in Search Console and monitor indexing.
