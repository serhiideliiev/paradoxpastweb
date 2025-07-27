#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Development configuration for Project Paradox Past.

This configuration imports the base settings and overrides
specific values for local development.
"""

# Import all settings from the base configuration
# pylint: disable=wildcard-import,unused-wildcard-import
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from pelicanconf import *  # noqa: F401,F403

# =============================================================================
# DEVELOPMENT OVERRIDES
# =============================================================================

# Local development URL
SITEURL = 'http://127.0.0.1:8000'

# Enable relative URLs for local development
RELATIVE_URLS = True

# Keep search engines away during development
ROBOTS = 'noindex, nofollow'

# Disable feeds during development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

# Development-specific settings
DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False

# Enable debug features
DEBUG = True
