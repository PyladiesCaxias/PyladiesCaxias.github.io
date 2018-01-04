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
THEME = 'theme/bootstrap2'

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

MENUITEMS = (
    # ('Blog', '/archives.html'),
    # ('Materiais', '/materiais.html'),
)


LINKS = (('Python.org', 'http://python.org/'),
         ('Python Brasil', 'http://python.org.br/'),
         ('PyLadiesBrasil', 'http://brasil.pyladies.com/'),)

# Blogroll
SOCIAL = (('facebook-square', 'Facebook','https://www.facebook.com/pyladiescaxias/'),
         ('github-square', 'GitHub','https://github.com/PyladiesCaxias'),
         ('whatsapp','Whatsapp', 'https://chat.whatsapp.com/6zWbhXYgPWsEa8G03QJo0b'),
         ('slack', 'Slack PyLadiesRS', 'https://join.slack.com/t/pyladiesrs/shared_invite/enQtMjQ1ODQyOTQ0OTYyLWFhZTBjYTVmMzk0ZTA0OWI0ZjhjMzM1YTE1YzkyZWIxMjlmYjM3YTY0YmM3ZmRjZjg2NTZlZWEwNTA4ZmJiNWY'),
         ('meetup', 'Meetup', 'https://www.meetup.com/pt-BR/PyLadies-CaxiasdoSul/'),)

EMAIL = ('envelope','caxiasdosul@pyladies.com', 'mailto:caxiasdosul@pyladies.com')

EVENTOS = (('Python Brasil[14] - 2018', 'http://2018.pythonbrasil.org.br/'),
    ('PyCaxias', 'http://pycaxias.org/'),
    ('Python Sul', 'http://pythonsul.org/'),)

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ['plugins']
PLUGINS = ['events', 'pelican_youtube', 'tag_cloud']

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True

PLUGIN_EVENTS = {
    'ics_fname': 'calendar.ics',

}
