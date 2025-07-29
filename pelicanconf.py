#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pelican configuration file for Project Paradox Past.

This configuration follows PEP-8 and Pelican best practices.
"""

from datetime import datetime

# =============================================================================
# BASIC SITE INFORMATION
# =============================================================================

AUTHOR = 'Paradox Past'
SITENAME = 'Project Paradox Past'
SITEURL = 'https://paradoxpast.me'
SITEDESCRIPTION = (
    'A digital space exploring the intersections of history, '
    'technology, and storytelling'
)

# Dynamic year for copyright
CURRENT_YEAR = datetime.now().year

# Site metadata
SITETITLE = SITENAME
SITESUBTITLE = 'Where past meets present in fascinating ways'
SITELOGO = 'images/logo.png'  # Project logo for header
FAVICON = 'images/favicon.ico'  # Favicon for browser tab

# =============================================================================
# CONTENT CONFIGURATION
# =============================================================================

# Content paths
PATH = 'content'
OUTPUT_PATH = 'output/'
STATIC_PATHS = ['images', 'extra', 'admin']
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# Content processing
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

# Article and page URL patterns
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# =============================================================================
# THEME CONFIGURATION
# =============================================================================

THEME = 'themes/custom'

# Theme-specific settings
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False  # Disabled to simplify navigation

# Disable unnecessary page generation (Pelican Flex minimalist approach)
AUTHOR_SAVE_AS = ''  # Disable individual author pages
AUTHORS_SAVE_AS = ''  # Disable authors index
CATEGORY_SAVE_AS = ''  # Disable individual category pages  
CATEGORIES_SAVE_AS = ''  # Disable categories index
TAG_SAVE_AS = ''  # Disable individual tag pages
TAGS_SAVE_AS = ''  # Disable tags index

# Keep only essential pages
DIRECT_TEMPLATES = ['index', 'articles', 'archives']  # Homepage, articles, and archives (archives hidden from nav)
PAGINATED_TEMPLATES = {
    'index': None,  # No pagination on homepage
    'archives': None,  # No pagination on archives (we handle this in template)
}

# Navigation menu items (simplified)
MENUITEMS = (
    ('Archives', '/archives.html'),
)

# Social links
SOCIAL = (
    ('tiktok', 'https://tiktok.com/@yourusername'),  # Replace with your actual TikTok URL
    ('instagram', 'https://instagram.com/yourusername'),  # Replace with your actual Instagram URL
)

# Custom CSS
CUSTOM_CSS = 'theme/css/homepage.css'

# =============================================================================
# FEED CONFIGURATION
# =============================================================================

# Feed generation is disabled during development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# =============================================================================
# PAGINATION AND ORGANIZATION
# =============================================================================

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Article organization
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True

# =============================================================================
# OUTPUT CONFIGURATION
# =============================================================================

DELETE_OUTPUT_DIRECTORY = True

# Extra path metadata for special files
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/.nojekyll': {'path': '.nojekyll'},
}

# =============================================================================
# SEO AND METADATA
# =============================================================================

# Search engine settings
ROBOTS = 'noindex, nofollow'  # Change to 'index, follow' for production

# Open Graph and Twitter Card metadata
OG_LOCALE = 'en_US'
TWITTER_USERNAME = 'paradoxpast'  # TODO: Update when Twitter account created

# =============================================================================
# PLUGIN CONFIGURATION
# =============================================================================

# Plugin paths and enabled plugins
PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = [
#     'sitemap',
#     'neighbors',
#     'series',
# ]

# Sitemap plugin configuration (disabled until site is ready)
# SITEMAP = {
#     'format': 'xml',
#     'priorities': {
#         'articles': 0.7,
#         'indexes': 0.9,
#         'pages': 0.6
#     },
#     'changefreqs': {
#         'articles': 'weekly',
#         'indexes': 'daily',
#         'pages': 'monthly'
#     }
# }

# =============================================================================
# DEVELOPMENT SETTINGS
# =============================================================================

# Uncomment for development with relative URLs
# RELATIVE_URLS = True

# Copyright notice
COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = AUTHOR
