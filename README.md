# Project Paradox Past - Development Guide

## Overview

This is a Pelican static site generator project for exploring historical paradoxes and temporal mysteries. The project follows modern Python development practices, PEP-8 compliance, and professional web development standards.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager
- Git (for deployment)

### Installation

1. **Clone and setup:**
   ```bash
   git clone https://github.com/serhiideliiev/paradoxpastweb.git
   cd project_paradox_past_website
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   make install
   ```

3. **Start development:**
   ```bash
   make devserver
   ```
   Visit: http://localhost:8000

### Quick Commands

```bash
# Install dependencies
make install

# Generate site for development
make html

# Start development server
make serve

# Generate and serve in one command
make devserver

# Clean generated files
make clean

# Format Python code
make format

# Lint Python code
make lint

# Deploy to GitHub Pages
make github
```

## 📁 Project Structure

```
project_paradox_past_website/
├── .github/workflows/          # GitHub Actions CI/CD
│   └── deploy-pelican.yml     # Automated deployment
├── content/                   # Markdown content files
│   ├── extra/                # Static files (robots.txt, CNAME)
│   ├── images/               # Content images
│   └── *.md                  # Articles/posts
├── themes/
│   └── custom/               # Minimalist custom theme (Pelican Flex approach)
│       ├── static/css/       # Essential CSS only
│       └── templates/        # Core templates only
│           ├── base.html     # Base template
│           ├── index.html    # Homepage
│           ├── article.html  # Individual articles
│           ├── page.html     # Static pages
│           ├── archives.html # Articles catalog
│           └── partial/      # Essential partials only
├── pelicanconf.py            # Main configuration (PEP-8 compliant)
├── pelicanconf_dev.py        # Development configuration
├── publishconf.py            # Production configuration
├── Makefile                  # Development workflow automation
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore rules
```

### Template Optimization

Following Pelican Flex theme best practices, we use a **minimalist approach** with only essential templates:

**Core Templates (5):**
- `base.html` - Base layout with navigation and footer
- `index.html` - Homepage with hero section and featured content  
- `article.html` - Individual article pages
- `page.html` - Static pages
- `archives.html` - Beautiful articles catalog page

**Essential Partials (11):**
- `og_article.html` - Open Graph meta tags for articles
- `translations.html` - Multi-language support
- `share_post.html` - Social sharing buttons
- `neighbors.html` - Previous/next article navigation
- `disqus.html` & `isso.html` - Comments integration
- `cc_license.html`, `copyright.html`, `footer.html` - Footer components
- `flex.html`, `statuscake.html` - Theme utilities

**Disabled Features (for simplicity):**
- Author pages - Redirected to homepage
- Category pages - Content accessible via archives
- Tag pages - Content accessible via archives  
- Search functionality - Simplified navigation focus

## 🎨 Design System

### Color Palette
- **Primary Blue:** `#5b72ee`
- **Secondary Purple:** `#9333ea`
- **Orange:** `#f59e0b`
- **Pink:** `#ec4899`
- **Text Colors:** `#1f2937` (dark), `#6b7280` (gray), `#9ca3af` (light)

### Typography
- **Font Family:** Inter (Google Fonts)
- **Weights:** 300, 400, 500, 600, 700

### Components
- **Hero Section:** Two-column layout with CTA
- **Paradox Cards:** Three-column grid with gradients
- **Timeline:** Vertical timeline with events
- **Newsletter:** Gradient background with signup
- **Articles:** Three-column article grid

## 🛠 Configuration

### Custom Domain Setup
1. Add `CNAME` file in `content/extra/` with your domain
2. Configure DNS with these records:
   ```
   Type: A, Host: @, Value: 185.199.108.153
   Type: A, Host: @, Value: 185.199.109.153
   Type: A, Host: @, Value: 185.199.110.153
   Type: A, Host: @, Value: 185.199.111.153
   Type: CNAME, Host: www, Value: serhiideliiev.github.io
   ```

### Environment Variables
- Update `SITEURL` in `pelicanconf.py` for your domain
- Update social links in `SOCIAL` configuration
- Replace email address in social links

## 🔧 Development

### Adding Content
1. Create `.md` files in `content/`
2. Use frontmatter for metadata:
   ```markdown
   Title: Your Post Title
   Date: 2024-01-01 10:00
   Category: Technology
   Tags: tag1, tag2
   Slug: your-post-slug
   
   Your content here...
   ```

### Customizing Design
- Modify CSS components in `themes/custom/static/css/components/`
- Update templates in `themes/custom/templates/`
- CSS is modular - edit individual component files

### Adding Features
- Install Pelican plugins via `pip`
- Add plugin names to `PLUGINS` in `pelicanconf.py`
- Configure plugin settings as needed

## 📦 Deployment

### Automatic Deployment
- Pushes to `main` branch trigger GitHub Actions
- Site deploys automatically to GitHub Pages
- Custom domain configured via CNAME

### Manual Deployment
```bash
pelican content
# Upload output/ directory to web server
```

## 🔍 SEO & Performance

- Semantic HTML structure
- Meta tags for social sharing
- Mobile-responsive design
- Fast loading with optimized CSS
- Search engine friendly URLs

## 📝 License

This project is open source. Feel free to use it as a template for your own sites.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

---

Built with ❤️ using [Pelican](https://getpelican.com/) and deployed on [GitHub Pages](https://pages.github.com/)
