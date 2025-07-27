# Decap CMS Setup Guide for Custom Domain

When you're ready to migrate to your custom domain, follow these steps to add Decap CMS for web-based content management.

## Prerequisites
- Custom domain configured and working
- GitHub Pages or Netlify hosting
- Site running on your custom domain

## Setup Steps

### 1. Create Admin Directory
Create these files in your project:

```
content/
├── admin/
│   ├── index.html
│   └── config.yml
```

### 2. Admin Interface (content/admin/index.html)
```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Content Manager</title>
  <script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
</head>
<body>
  <!-- Include the script that builds the page and powers Decap CMS -->
  <script src="https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js"></script>
</body>
</html>
```

### 3. CMS Configuration (content/admin/config.yml)
```yaml
backend:
  name: github
  repo: serhiideliiev/paradoxpastweb
  branch: main

media_folder: "content/images"
public_folder: "/images"

collections:
  - name: "blog"
    label: "Blog Posts"
    folder: "content"
    create: true
    slug: "{{slug}}"
    fields:
      - {label: "Title", name: "title", widget: "string"}
      - {label: "Date", name: "date", widget: "datetime"}
      - {label: "Category", name: "category", widget: "string", default: "Blog"}
      - {label: "Tags", name: "tags", widget: "list"}
      - {label: "Slug", name: "slug", widget: "string"}
      - {label: "Authors", name: "authors", widget: "string", default: "Paradox Past"}
      - {label: "Summary", name: "summary", widget: "text"}
      - {label: "Body", name: "body", widget: "markdown"}
```

### 4. Update Pelican Configuration
Add to `pelicanconf.py`:
```python
# Static paths for admin interface
STATIC_PATHS = ['images', 'extra', 'admin']

# Extra path metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'admin/index.html': {'path': 'admin/index.html'},
    'admin/config.yml': {'path': 'admin/config.yml'},
}
```

### 5. GitHub OAuth App Setup
1. Go to GitHub Settings → Developer settings → OAuth Apps
2. Create new OAuth App with:
   - Homepage URL: `https://your-domain.com`
   - Authorization callback URL: `https://api.netlify.com/auth/done`
3. Note the Client ID and Client Secret

### 6. Authentication Setup
Choose one:
- **Option A**: Use Netlify Identity (recommended)
- **Option B**: Use GitHub OAuth directly

### 7. Access Your CMS
After setup, access at: `https://your-domain.com/admin/`

## Benefits You'll Get
- ✅ Web-based content editor
- ✅ Rich text editing with live preview
- ✅ Media upload and management
- ✅ No need to touch code for blog posts
- ✅ Mobile-friendly admin interface
- ✅ Collaborative editing capabilities

## Notes
- Works with any custom domain
- Completely free to use
- Integrates seamlessly with your current Pelican setup
- No database required - everything stored in your GitHub repo
