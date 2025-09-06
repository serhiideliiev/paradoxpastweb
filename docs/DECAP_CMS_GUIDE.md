# Decap CMS Setup Guide - Project Paradox Past

## What is Decap CMS?

Decap CMS (formerly Netlify CMS) is a content management system that provides a user-friendly admin interface for managing your static site content. It allows you to create, edit, and publish articles without touching code.

## Setup Instructions

### 1. Authentication Setup

Since your site is hosted on GitHub Pages, you'll need to set up authentication. You have two main options:

#### Option A: Netlify Identity (Recommended)
1. Create a free Netlify account at https://netlify.com
2. Connect your GitHub repository to Netlify
3. Go to Site Settings > Identity and enable it
4. Set up your admin user through the Netlify dashboard
5. Enable Git Gateway in Identity settings

#### Option B: GitHub OAuth App
1. Go to GitHub Settings > Developer settings > OAuth Apps
2. Create a new OAuth app with:
   - Application name: Project Paradox Past CMS
   - Homepage URL: https://paradoxpast.me
   - Authorization callback URL: https://paradoxpast.me/admin/
3. Update the config.yml backend settings with your client ID

### 2. Accessing the CMS

Once authentication is set up:
1. Visit https://paradoxpast.me/admin/
2. Log in with your credentials
3. Start creating and editing content!

## CMS Features

### Content Management
- **Articles**: Create and edit blog articles with categories, tags, and featured images
- **Pages**: Manage static pages like About, Contact, etc.
- **Settings**: Edit site configuration directly from the admin interface

### Editorial Workflow
- Draft articles before publishing
- Review and approve content
- Schedule publication dates

### Media Management
- Upload and organize images
- Automatic image optimization
- Easy insertion into articles

## File Structure

```
content/
├── admin/
│   ├── index.html          # CMS admin interface
│   ├── config.yml          # CMS configuration
│   └── redirect.html       # Authentication redirect
├── articles/               # Article markdown files
├── pages/                  # Static page files
└── images/                 # Media files
```

## Writing Articles

### Front Matter Fields
Each article includes metadata:
- **Title**: Article headline
- **Date**: Publication date
- **Category**: History, Science, Technology, Culture, Mystery
- **Tags**: Keywords for organization
- **Slug**: URL-friendly identifier
- **Author**: Byline (defaults to "Project Paradox Past Team")
- **Summary**: Brief description for previews
- **Image**: Featured image (optional)
- **Status**: published or draft

### Markdown Content
Write your article content in Markdown format with support for:
- Headers (# ## ###)
- **Bold** and *italic* text
- [Links](https://example.com)
- Images ![alt text](image-url)
- Lists and quotes
- Code blocks

## Workflow

1. **Create**: Use the CMS to create new articles
2. **Draft**: Save as draft while working
3. **Preview**: Review your content formatting
4. **Publish**: Change status to "published"
5. **Deploy**: Changes automatically deploy via GitHub Actions

## Best Practices

### Content Organization
- Use descriptive slugs for SEO
- Add relevant tags for discoverability
- Write compelling summaries
- Include featured images when possible

### Writing Style
- Start with engaging hooks
- Use subheadings to break up text
- Include questions to encourage engagement
- End with thought-provoking conclusions

### SEO Optimization
- Use keywords naturally in titles and content
- Write meta descriptions (summaries)
- Optimize images with alt text
- Use internal linking between articles

## Troubleshooting

### Common Issues
1. **Can't access admin**: Check authentication setup
2. **Changes not appearing**: Wait for GitHub Actions deployment (2-3 minutes)
3. **Images not loading**: Ensure proper image paths
4. **Formatting issues**: Review Markdown syntax

### Getting Help
- Check the [Decap CMS documentation](https://decapcms.org/docs/)
- Review GitHub repository issues
- Test changes locally with `pelican --listen`

## Local Development

To test CMS changes locally:
1. Enable local backend in config.yml
2. Run `npx decap-server` in a separate terminal
3. Start Pelican development server
4. Access admin at http://localhost:8000/admin/

---

**Happy writing! Your content management system is ready to help you create amazing articles about history's most fascinating paradoxes.**
