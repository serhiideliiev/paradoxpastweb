# Pelican Static Site with GitHub Actions Deployment

This repository contains a Pelican static site with automated deployment to GitHub Pages using GitHub Actions.

## Setup Instructions

### 1. Repository Setup

1. Fork or clone this repository
2. Go to your repository settings on GitHub
3. Navigate to **Pages** in the left sidebar
4. Under **Source**, select "GitHub Actions"

### 2. Configuration

1. **Edit `pelicanconf.py`**: Update the site information (name, author, etc.)
2. **Update SITEURL**: Set the correct URL for your GitHub Pages site:

   ```python
   SITEURL = 'https://yourusername.github.io/your-repo-name'
   ```

### 3. Content Creation

- Add your content files to the `content/` directory
- Use Markdown format with Pelican metadata headers
- Images and other static files go in `content/images/` or `content/extra/`

### 4. Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Generate the site
pelican content -s pelicanconf.py

# Serve locally (optional)
pelican --listen --autoreload
```

## GitHub Actions Workflow

The workflow (`.github/workflows/deploy-pelican.yml`) includes:

### Features

- **Automatic Deployment**: Triggers on pushes to the `main` branch
- **Python Environment**: Sets up Python 3.11
- **Dependency Caching**: Caches pip dependencies for faster builds
- **Site Generation**: Runs Pelican to generate static files
- **GitHub Pages Deployment**: Automatically deploys to GitHub Pages

### Two Deployment Options

The workflow provides two deployment methods:

1. **Default**: Uses the official `actions/deploy-pages` action (recommended)
2. **Alternative**: Uses `peaceiris/actions-gh-pages` action (set `if: false` to `if: true` to enable)

### Workflow Steps

1. **Build Job**:
   - Checkout repository
   - Set up Python environment
   - Cache dependencies
   - Install Pelican and dependencies
   - Generate the site
   - Upload artifacts

2. **Deploy Job**:
   - Deploy to GitHub Pages using the built artifacts

## Customization

### Adding Dependencies

Add any additional Python packages to `requirements.txt`:

```txt
pelican[markdown]>=4.8.0
your-package-name>=1.0.0
```

### Pelican Configuration

Modify `pelicanconf.py` to customize:
- Site metadata
- URL structure
- Themes and plugins
- Static file handling

### Workflow Customization

You can modify the workflow to:
- Change Python version
- Add additional build steps
- Customize deployment settings
- Add environment-specific configurations

## Troubleshooting

### Common Issues

1. **Output directory not created**: Check that `pelicanconf.py` is properly configured
2. **Dependencies not found**: Ensure all required packages are in `requirements.txt`
3. **Deployment fails**: Verify that GitHub Pages is enabled in repository settings

### Debugging

- Check the Actions tab in your GitHub repository for workflow runs
- Review the build logs for specific error messages
- Test locally before pushing changes

## File Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy-pelican.yml    # GitHub Actions workflow
├── content/                      # Your content files
│   ├── images/                   # Static images
│   └── welcome.md               # Sample content
├── pelicanconf.py               # Pelican configuration
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Resources

- [Pelican Documentation](https://docs.getpelican.com/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
