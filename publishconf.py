#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Production configuration for Project Paradox Past.

This configuration imports the base settings and overrides
specific values for production deployment.
"""

# Import all settings from the base configuration
# pylint: disable=wildcard-import,unused-wildcard-import
from pelicanconf import *  # noqa: F401,F403

# =============================================================================
# PRODUCTION OVERRIDES
# =============================================================================

# Ensure production URL is set
SITEURL = 'https://paradoxpast.me'

# Enable all feeds for production
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None

# Enable search engine indexing
ROBOTS = 'index, follow'

# Disable relative URLs for production
RELATIVE_URLS = False

# Enable Google Analytics (when ready)
# GOOGLE_ANALYTICS = 'G-XXXXXXXXXX'

# Enable other production-specific features
DELETE_OUTPUT_DIRECTORY = True

# Performance optimizations
LOAD_CONTENT_CACHE = True
