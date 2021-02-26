"""
Base settings to build other settings files upon.
"""

import os
import environ

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ------------------------------------------------------------------------------
# DJANGO ENV SETTINGS
# ------------------------------------------------------------------------------

# Settings for Django-environ
# https://django-environ.readthedocs.io/en/latest/#
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Reading .env file
environ.Env.read_env()

# ------------------------------------------------------------------------------
# GENERAL
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env("DJANGO_DEBUG")

# https://docs.djangoproject.com/en/3.1/ref/contrib/messages/
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = "GB"

# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-GB"

# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(BASE_DIR / "locale")]

# ------------------------------------------------------------------------------
# URLS
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'core.urls'

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'core.wsgi.application'

# ------------------------------------------------------------------------------
# APPS
# ------------------------------------------------------------------------------

DJANGO_APPS = [
    'django_admin_env_notice',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "django.contrib.humanize",
    "django.forms",
]

# THIRD_PARTY_APPS = [
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
# ]

LOCAL_APPS = [
    'users',
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

# ------------------------------------------------------------------------------
# AUTHENTICATION
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
# AUTHENTICATION_BACKENDS = [
#     "django.contrib.auth.backends.ModelBackend",
#     "allauth.account.auth_backends.AuthenticationBackend",
# ]

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'users.CustomUser'

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
# LOGIN_REDIRECT_URL = "users:redirect"

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
# LOGIN_URL = "account_login"

# ------------------------------------------------------------------------------
# MIDDLEWARE
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ------------------------------------------------------------------------------
# PASSWORDS
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},  # noqa
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},  # noqa
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},  # noqa
]

# ------------------------------------------------------------------------------
# TEMPLATES
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.tz',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        }
    }
]

# ------------------------------------------------------------------------------
# SECURITY
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True

# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# ------------------------------------------------------------------------------
# ADMIN
# ------------------------------------------------------------------------------

# Django Admin URL.
# ADMIN_URL = env("DJANGO_ADMIN_URL", "admin/")

# ------------------------------------------------------------------------------
# LOGGING
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# ------------------------------------------------------------------------------
# django-allauth
# ------------------------------------------------------------------------------
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True) # noqa
# 
# ACCOUNT_AUTHENTICATION_METHOD = "username"
# 
# ACCOUNT_EMAIL_REQUIRED = True
#
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# 
# ACCOUNT_ADAPTER = "{{cookiecutter.project_slug}}.users.adapters.AccountAdapter" # noqa
# 
# SOCIALACCOUNT_ADAPTER = "{{cookiecutter.project_slug}}.users.adapters.SocialAccountAdapter" # noqa