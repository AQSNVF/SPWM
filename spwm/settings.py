import os
from decouple import config
from dj_database_url import parse as dburl
from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ALLOWED_HOSTS = [
    '18.216.162.32',
    '127.0.0.1',
    'localhost',
    'spwm.com.br'
]

INTERNAL_IPS = [
    '127.0.0.1',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.google',

    'rest_framework',
    'rest_framework.authtoken',
    'apps.empresas',
    'apps.funcionarios',
    'apps.departamentos',
    'apps.documentosfunc',
    'apps.registro_hora_extra',
    'apps.spwm_ws',
    'bootstrapform',
    'django_celery_results',
    'django_celery_beat',
    'apps.spwm_welding',
    'apps.spwm_pipe_cleaning',
    'debug_toolbar',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'spwm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'spwm.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_URL = 'home'

LOGIN_REDIRECT_URL = 'login/'

LOGOUT_REDIRECT_URL = 'login'

CELERY_RESULT_BACKEND = 'django-db'


CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

from .local_settings import *

#
# LANGUAGES = (
#     ('en', _('English')),
#     ('pt', _('Portugues')),
#     ('es', _('Spanish')),
# )
#
# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale'),
# )
#



# SERVER_EMAIL = 'nelson.freire@spwm.com.br'
# TITULO_SITE = 'Activates Quality Solutions'
# EMAIL_SUBJECT_PREFIX = 'Activates Quality Solutions '
# DEFAULT_FROM_EMAIL = 'nelson.freire@activates.com.br'



#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file':{
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level':'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = 'gestao-clientes'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'
#
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#
#

#
# #TODO: Endereço dos Templates do Admin
# #/home/nvf/UDEMY/venv/lib/python3.6/site-packages/django/contrib/admin/templates/
# # registration/password_change_form.html
#
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }