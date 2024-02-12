import os
from .settings import *

if 'WEBSITE_HOSTNAME' in os.environ:
    SECRET_KEY = os.environ['SECRET']
    ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
    CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']]
    DEBUG = False

    INSTALLED_APPS = [
        "whitenoise.runserver_nostatic",
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'text_retrieval'
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')
    STATIC_ROOT = BASE_DIR / "staticfiles"
