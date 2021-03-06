# settings/local.py
from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_HOST = "localhost"
#EMAIL_PORT = 1025

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'muhovyaz',
        'USER': 'muhovyaz',
        'PASSWORD': 'security',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

INSTALLED_APPS += ('debug_toolbar', )
#INTERNAL_IPS = ("127.0.0.1",)

#MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware", )
