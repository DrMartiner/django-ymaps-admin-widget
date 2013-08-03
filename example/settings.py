# -*- coding: utf-8 -*-

import sys
import os.path

try:
    from settings_local import *
except ImportError:
    print "Don't forget create settings_local.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, '..'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'ymap_example',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = 'SECRET_KEY'
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
)

INSTALLED_APPS = (
    'django.contrib.gis',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'yandexmaps_widget',
    'app',
)

try:
    from settings_local import *
except ImportError:
    pass