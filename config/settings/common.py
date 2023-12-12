"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from datetime import timedelta
from glob import glob
from typing import Dict

import django
import environ  # noqa
import sentry_sdk
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from firebase_admin import credentials, initialize_app
from rest_framework import status
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

################################
env = environ.Env()
env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = environ.Path(__file__) - 3

BASE_URL = env("BASE_URL", default="http://localhost")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ybf)8sva8d18ko8p*iczdg)5i9h-2c7v1et*59itd41s!z-998'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.core.apps.CoreConfig',
    'apps.users.apps.UsersConfig',
    'apps.users_auth.apps.UsersAuthConfig',
    'apps.blogs.apps.BlogsConfig',
]

THIRD_APPS = [
    "rest_framework",
    # Auth
    "rest_framework.authtoken",
    "dj_rest_auth",
    # Registration
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    # Swagger
    "drf_yasg",
]

INSTALLED_APPS = THIRD_APPS + LOCAL_APPS + INSTALLED_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Auth model
AUTH_USER_MODEL = "users.User"

# Route
ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": env.db("DATABASE_URL", default=""),
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = env.str("STATIC_ROOT", default=str(ROOT_DIR("staticfiles")))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
STATICFILES_DIRS = (str(ROOT_DIR("static")),)

# Media
MEDIA_ROOT = env.str("MEDIA_ROOT", default=str(ROOT_DIR("media")))
MEDIA_URL = env("MEDIA_URL", default="/media/")
TEMP_FILE_URL = env("TEMP_FILE_URL", default=str(ROOT_DIR("media")))

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WSGI_APPLICATION = "config.wsgi.application"

# Registration
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = "all"  # all , email or username
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False