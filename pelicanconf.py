#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'PyLadies'
SITENAME = u'PyLadies Caxias do Sul'
SITELOGO = 'images/icones/desenho3.png'
SITEURL = 'http://localhost:8000'
TAGLINE = (u'Ninguém pode fazer você se sentir inferior'
           'sem o seu consentimento (Eleanor Roosevelt)')
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')
DEFAULT_BG = 'images/logo.jpg'
DATE_TODAY = datetime.now().date()
SUMMARY_MAX_LENGTH = 60
APP_ID_FACEBOOK = 'pyladiescaxias'
API_KEY_MEETUP = '772b514b2dbe5e5d335895f47072'
ID_MEETUP = 'PyLadies-CaxiasdoSul'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

PATH = 'content'

DEFAULT_METADATA = {'Status': 'published'}

STATIC_PATHS = ['images', 'extra/CNAME', 'icones/logo.ico', 'pdfs']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'
THEME = 'theme/voce'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GOOGLE_CUSTOM_SEARCH_SIDEBAR = False
TWITTER_USERNAME = False

# GOOGLE_ANALYTICS_ID: Your Google Analytics UA-XXXXXXXX-X code (None to disable analytics).
# GOOGLE_ANALYTICS_PROP: Your Google Analytics property name (None to disable analytics).
USER_LOGO_URL = 'images/icones/desenho3.png'
MANGLE_EMAILS = True
# GLOBAL_KEYWORDS: A list of strings that will be set as meta keywords for each page.
FUZZY_DATES = True

TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'

SOCIAL = (('Feed','/feeds/all.atom.xml'),
      ('Email','mailto:xxx@gmail.com'),
      ('GitHub','http://github.com/limbenjamin'),)

LINKS = (
        ('Home','/index.html'),
        ('Sobre','/sobre/index.html'),
        ('Materiais','/materiais/index.html'),
        ('Eventos','/events-list/index.html'),
        )

SOCIAL = (
    ('Email','mailto:caxiasdosul@pyladies.com'),
    ('Facebook','https://www.facebook.com/pyladiescaxias/'),
    ('GitHub','https://github.com/PyladiesCaxias'),
    ('meetup', 'https://www.meetup.com/pt-BR/PyLadies-CaxiasdoSul/'),
)

MATERIAIS_LINKS = (('Django Project', 'https://docs.djangoproject.com/en/1.8/intro/tutorial01/', 'Python/Django'),
    ('Code Academy Python course', 'https://www.codecademy.com/en/tracks/python', 'Python'),
    ('Code Academy HTML & CSS course', 'https://www.codecademy.com/tracks/web', 'Web'),
    ('Django Carrots tutorial', 'https://github.com/ggcarrots/django-carrots/', 'Python/Django'),
    ('Getting Started With Django video lessons', 'http://www.gettingstartedwithdjango.com/', 'Python/Django'),
    ('Python para Zumbis', 'https://www.pycursos.com/python-para-zumbis/', 'Python'),
    ('Pycursos', 'https://www.pycursos.com/', 'Python'),
    ('Python 3 na web com Django', 'https://www.udemy.com/python-3-na-web-com-django-basico-intermediario/', 'Python/Django'),
)
DEFAULT_PAGINATION = 10
PDF_PROCESSOR = None

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican_youtube', 'tag_cloud', 'assets']

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True
