from dotenv import load_dotenv

load_dotenv()

import os
from pathlib import Path
from decouple import config
import dj_database_url
import django_heroku
from whitenoise.middleware import WhiteNoiseMiddleware
from whitenoise.storage import CompressedManifestStaticFilesStorage
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

manifest_path = os.path.join(BASE_DIR, 'staticfiles', 'manifest.json')
staticfiles_storage = CompressedManifestStaticFilesStorage(location=manifest_path)

print(staticfiles_storage.manifest)


SECRET_KEY = config('SECRET_KEY')
DEBUG = False
DATABASE_URL = config('DATABASE_URL')


ALLOWED_HOSTS = [
    "tasktales-e12d965b0fbc.herokuapp.com",
    "127.0.0.1",
]



INSTALLED_APPS = [
    "tasks.apps.TasksConfig",
    "projects.apps.ProjectsConfig",
    "accounts.apps.AccountsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tracker.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tracker.wsgi.application"


DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]



LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True




STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


django_heroku.settings(locals())