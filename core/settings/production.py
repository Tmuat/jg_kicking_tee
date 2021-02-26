from .base import env
from .base import *  # noqa


# ------------------------------------------------------------------------------
# GENERAL
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
DJANGO_ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS').split(",")
ALLOWED_HOSTS = list(DJANGO_ALLOWED_HOSTS)

# ------------------------------------------------------------------------------
# DATABASES
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL')
             }

# ------------------------------------------------------------------------------
# SECURITY
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

# ------------------------------------------------------------------------------
# STORAGES
# ------------------------------------------------------------------------------

# https://django-storages.readthedocs.io/en/latest/#installation
# INSTALLED_APPS += ["storages"]  # noqa F405

# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")

# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")

# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")

# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_OBJECT_PARAMETERS = {
#     'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#     'CacheControl': 'max-age=94608000',
# }

# ------------------------------------------------------------------------------
# STATIC
# ------------------------------------------------------------------------------
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
# STATICFILES_LOCATION = 'static'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'

# ------------------------------------------------------------------------------
# MEDIA
# ------------------------------------------------------------------------------
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
# MEDIAFILES_LOCATION = 'media'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# ------------------------------------------------------------------------------
# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
# DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
# EMAIL_BACKEND = 'django_ses.SESBackend'

# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
# AWS_SES_REGION_NAME = env('AWS_SES_REGION_NAME')
# AWS_SES_REGION_ENDPOINT = env('AWS_SES_REGION_ENDPOINT')

# ------------------------------------------------------------------------------
# Sentry
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# ENVIRONMENT NOTICE
# ------------------------------------------------------------------------------
# https://pypi.org/project/django-admin-env-notice/
ENVIRONMENT_NAME = "Production server"
ENVIRONMENT_COLOR = "#0AD12C"
