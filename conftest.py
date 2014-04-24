import os
import sys

SECRET_KEY = 'test - secret - key'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'HOST': '',
        'PORT': '',
        'USER': ''},
}

INSTALLED_APPS = ['whatsnew', ]


def pytest_configure(config):
    here = os.path.dirname(__file__)
    sys.path.insert(0, here)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'conftest'
    # from django.conf import settings
