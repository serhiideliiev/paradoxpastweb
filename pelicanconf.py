#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Basic site information
AUTHOR = 'Paradox Past'
SITENAME = 'Project Paradox Past'  
SITEURL = 'https://serhiideliiev.github.io/paradoxpastweb'

# Content settings
PATH = 'content'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

# Feed generation (usually disabled for development)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Output settings
OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = True

# URL and save as patterns
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'

# Static paths
STATIC_PATHS = ['images', 'extra']

# Theme settings (uncomment and modify as needed)
# THEME = 'path-to-your-theme'

# Plugin settings (uncomment and modify as needed)
# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['sitemap', 'neighbors']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
