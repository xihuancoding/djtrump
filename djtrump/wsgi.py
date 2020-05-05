"""
WSGI config for djtrump project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

import sys

sys.path.append('/home/abcd/www/djtrump')

sys.path.append('/home/abcd/www/venv/lib/python3.7/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djtrump.settings")

application = get_wsgi_application()
