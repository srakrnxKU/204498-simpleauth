"""
WSGI config for simple_auth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/html/simpleauth')
sys.path.append('/var/www/html/simpleauth/simple_auth')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_auth.settings')

application = get_wsgi_application()
