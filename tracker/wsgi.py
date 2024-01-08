"""
WSGI config for tracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
import django_heroku
from pathlib import Path



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tracker.settings")


application = get_wsgi_application()
application = WhiteNoise(application)

BASE_DIR = Path(__file__).resolve().parent.parent



# django_heroku.settings(locals())

# Change this line:
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# To this line:
