"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from core.settings.base import DJANGO_SETTINGS_MODULE_ENV

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      DJANGO_SETTINGS_MODULE_ENV)

application = get_wsgi_application()
