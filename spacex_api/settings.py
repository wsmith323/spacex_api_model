import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'secret_key_for_development')

# Default would be False for a real app.
DEBUG = os.environ.get('DJANGO_DEBUG', True)

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'spacex_api',
]

# Setup sessions if necessary.
if DEBUG:
    # Use database for session storage for development.
    INSTALLED_APPS.insert(1, 'django.contrib.sessions')
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'
else:
    # Use something like Redis for session storage in production.
    SESSION_ENGINE = 'redis_sessions.session'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spacex_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'spacex_api.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en-us'

USE_TZ = True
TIME_ZONE = 'UTC'

STATIC_URL = '/static/'

SPACEX_API_URL_PREFIX = os.environ.get('SPACEX_API_URL_PREFIX', 'https://api.spacexdata.com/v4')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'minimal',
        },
        'null': {
            'class': 'logging.NullHandler',
        }
    },
    'formatters': {
        'minimal': {
            'format': '[{asctime}] {name}: {message}',
            'style': '{',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'WARNING',
    },
    'loggers': {
        #
        # Silence logging we don't care about.
        #
        'asyncio': {
            'handlers': ['null'],
            'propagate': False,
        }
        #
        # Would need to configure additional logging in production.
        #
    },
}
