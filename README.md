# Project Paradox Past

A minimalist Pelican static site exploring historical paradoxes and temporal mysteries.

## Quick Start

```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Development
PELICAN_ENV=development pelican content -s config.py -r -l

# Production Build
PELICAN_ENV=production pelican content -s config.py

# Deploy
git push origin main  # Auto-deploys via GitHub Actions
```
## Structure

- `content/articles/` - Blog posts
- `content/admin/` - CMS interface 
- `theme/` - Custom Pelican theme
- `config.py` - Unified configuration

## CMS Access

Visit `/admin/` to manage content via Decap CMS.

## License

Open source - feel free to fork and adapt.
