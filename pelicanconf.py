#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pyladies'
SITENAME = u'Pyladies Caxias'
SITELOGO = 'images/icones/desenho3.png'
SITEURL = 'http://localhost:8000'
TAGLINE = (u'Ninguém pode fazer você se sentir inferior'
           'sem o seu consentimento (Eleanor Roosevelt)')
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')
DEFAULT_BG = 'images/logo.jpg'


PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

PATH = 'content'
STATIC_PATHS = ['images', 'icones/logo.ico', 'pdfs']

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'
THEME = 'theme/bootstrap2'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


MENUITEMS = (
    # ('Blog', '/archives.html'),
    # ('Materiais', '/category/materiais.html'),
)


# Blogroll
LINKS = (('Python.org', 'http://python.org/'),
         ('Pyladies Brasil', 'http://brasil.pyladies.com/'),
         ('Python Brasil', 'http://python.org.br/'),)

# Blogroll
SOCIAL = (('facebook', 'https://www.facebook.com/Pyladies-Caxias-1858294514418047/'),
         ('github', 'https://github.com/PyladiesCaxias'),('pyladiescaxias@gmail.com', 'pyladiescaxias@gmail.com'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGINS = [
    'pelican_youtube'
]
