#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unified Pelican configuration for Project Paradox Past.
Supports both development and production environments.
"""

import os
from datetime import datetime

# =============================================================================
# ENVIRONMENT DETECTION
# =============================================================================

# Auto-detect environment or use PELICAN_ENV environment variable
ENVIRONMENT = os.getenv('PELICAN_ENV', 'development').lower()
IS_PRODUCTION = ENVIRONMENT == 'production'

# =============================================================================
# BASIC SITE INFORMATION
# =============================================================================

AUTHOR = 'Paradox Past'
SITENAME = 'Project Paradox Past'
SITEURL = 'https://paradoxpast.me' if IS_PRODUCTION else 'http://127.0.0.1:8000'
SITEDESCRIPTION = 'A digital space exploring the intersections of history, technology, and storytelling'

# Dynamic year for copyright
CURRENT_YEAR = datetime.now().year
SITETITLE = SITENAME
SITESUBTITLE = 'Where past meets present in fascinating ways'
SITELOGO = 'images/logo.png'
FAVICON = 'favicon.ico'

# =============================================================================
# CONTENT CONFIGURATION
# =============================================================================

PATH = 'content'
OUTPUT_PATH = 'output/'
STATIC_PATHS = ['images', 'extra', '_redirects', 'admin']
ARTICLE_PATHS = ['articles']

# Extra files to copy to output root
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    'extra/.nojekyll': {'path': '.nojekyll'},
    '_redirects': {'path': '_redirects'},
}

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

THEME = 'theme'

# Theme-specific settings
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Disable unnecessary page generation
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Keep only essential pages
DIRECT_TEMPLATES = ['index', 'articles', 'archives']
PAGINATED_TEMPLATES = {'index': None, 'archives': None}

# Navigation menu items
MENUITEMS = (('Archives', '/archives.html'),)

# Social links
SOCIAL = (
    ('tiktok', 'https://tiktok.com/@paradoxpastai'),
    ('instagram', 'https://instagram.com/paradoxpastai'),
)

# =============================================================================
# FEED CONFIGURATION
# =============================================================================

if IS_PRODUCTION:
    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds/category/{slug}.atom.xml'
else:
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# =============================================================================
# PAGINATION AND ORGANIZATION
# =============================================================================

DEFAULT_PAGINATION = 10
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True

# =============================================================================
# ENVIRONMENT-SPECIFIC SETTINGS
# =============================================================================

if IS_PRODUCTION:
    RELATIVE_URLS = False
    ROBOTS = 'index, follow'
    LOAD_CONTENT_CACHE = True
else:
    RELATIVE_URLS = True
    ROBOTS = 'noindex, nofollow'
    LOAD_CONTENT_CACHE = False
    DEBUG = True

# =============================================================================
# OUTPUT CONFIGURATION
# =============================================================================

DELETE_OUTPUT_DIRECTORY = True

# =============================================================================
# SEO AND METADATA
# =============================================================================

OG_LOCALE = 'en_US'
TWITTER_USERNAME = 'paradoxpast'

# Copyright notice
COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = AUTHOR
