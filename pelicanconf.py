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

# Flex theme specific settings
SITETITLE = 'Project Paradox Past'
SITESUBTITLE = 'Where past meets present in fascinating ways'
SITEDESCRIPTION = 'A digital space exploring the intersections of history, technology, and storytelling'
SITELOGO = None  # Add a logo URL here if you have one

# Social links for Flex theme (replaces old SOCIAL widget)
SOCIAL = (
    ('github', 'https://github.com/serhiideliiev'),
    ('envelope', 'mailto:your-email@example.com'),  # Replace with your email
)

DEFAULT_PAGINATION = 10

# Output settings
OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = True

# URL and save as patterns
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'

# Static paths
STATIC_PATHS = ['images', 'extra']

# Extra path metadata for robots.txt
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Theme settings
THEME = 'themes/Flex'

# Flex theme specific settings
SITETITLE = 'Project Paradox Past'
SITESUBTITLE = 'Where past meets present in fascinating ways'
SITEDESCRIPTION = 'A digital space exploring the intersections of history, technology, and storytelling'
SITELOGO = None  # Add a logo URL here if you have one

# Flex theme navigation
MAIN_MENU = True
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

# Prevent search engine indexing (remove when ready to go public)
ROBOTS = 'noindex, nofollow'

# Plugin settings (uncomment and modify as needed)
# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['sitemap', 'neighbors']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
