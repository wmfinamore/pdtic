from environs import Env
from pathlib import Path
import os
from import_export.formats.base_formats import XLSX, JSON, CSV
from smart_selects.widgets import JQUERY_URL

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
if DEBUG == False:
    CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')

# Application definition

INSTALLED_APPS = [

    # Package para módulo admin
    'config.apps.PdticAdminConfig',

    # Package nativas
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceiros
    'debug_toolbar',
    'simple_history',
    'crispy_forms',
    'crispy_bootstrap5',
    'import_export',
    'smart_selects',
    'sequences.apps.SequencesConfig',

    # App's
    'accounts',
    'apps.secretarias',
    'apps.core',
    'apps.equipes',
    'apps.relatorios',
    'apps.planos',
    'apps.swot',
    'apps.necessidades',
    'apps.metas',
    'apps.indicadores',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str("DB_NAME"),
        'USER': env.str("DB_USER"),
        'PASSWORD': env.str("DB_PASSWORD"),
        'HOST': env.str("DB_HOST"),
        'PORT': env.str("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/pdtic/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/pdtic/media/'

MEDIA_ROOT = BASE_DIR / 'mediafiles'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CONFIGURAÇÃO DO DEBUG TOOLBAR
INTERNAL_IPS = [
    '127.0.0.1',
]

# CONFIGURAÇÃO PARA USAR OUTRO USER MODEL DEFAULT
AUTH_USER_MODEL = 'accounts.CustomUser'

# # CONFIGURAÇÕES DE E-MAIL
# EMAIL_HOST = env.str('EMAIL_HOST')
# EMAIL_PORT = env.int('EMAIL_PORT')
# EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
# EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS')
#
# # ADMINS EMAIL
# ADMINS = [(env.str('ADMIN_NOME'), env.str('ADMIN_EMAIL')), ]

# Configurações de login/logout
LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'

LOGIN_URL = '/pdtic/accounts/login/'

# Configurações de Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env.list('REDIS_LOCATION'),
    }
}

CUSTOM_CACHE_TIME = env.int('CACHE_TIME')

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# IMPORT EXPORT CONFIGURATIONS
IMPORT_EXPORT_IMPORT_PERMISSION_CODE = ['add', 'change', ]  # permissões necessárias para importação
EXPORT_FORMATS = [XLSX, JSON, CSV]

# VALUE FORMAT
USE_THOUSAND_SEPARATOR = True

JQUERY_URL = env.str('JQUERY_URL')
