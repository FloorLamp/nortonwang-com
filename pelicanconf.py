#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Norton Wang'
SITENAME = u'Norton Wang'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

THEME = 'theme'

DISPLAY_CATEGORIES_ON_MENU = False

DIRECT_TEMPLATES = ('index', 'tags')

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MD_EXTENSIONS = ['codehilite(css_class=codehilite)']

#PLUGIN_PATH = 'home/wang/pelican-description'
#PLUGINS = ['description']
