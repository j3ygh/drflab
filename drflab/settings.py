"""
Django settings for drflab project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c_64whroi(mc8=w)zi=3p+8-571_2!)oql2#r#_(*dw+v*7a^6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # django rest framework
    'api.apps.ApiConfig',
    'crm.apps.CrmConfig',
    'usage.apps.UsageConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drflab.urls'

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

WSGI_APPLICATION = 'drflab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

ORACLE_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'drflabdb',
        'USER': 'system',
        'PASSWORD': 'User1234',
        'HOST': '10.50.12.21',
        'PORT': '1521',
    }
}

ORACLE_UTF8_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'drflabal32ut',
        'USER': 'system',
        'PASSWORD': 'User1234',
        'HOST': '10.50.12.21',
        'PORT': '1521',
    }
}

ORACLE_DATABASES_JEFF = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'db1',
        'USER': 'chief',
        'PASSWORD': 'User1234',
        'HOST': '10.50.12.21',
        'PORT': '1521',
    }
}

MARIA_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drflabdb',
        'USER': 'admin',
        'PASSWORD': '20180105',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

DATABASES = ORACLE_UTF8_DATABASES


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


# Django REST framework

LOGIN_NEEDED = False
BROWSABLEBAPI_NEEDED = True

REST_FRAMEWORK = {}
if LOGIN_NEEDED:
    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = [
        'rest_framework.permissions.DjangoModelPermissions',
    ]
if not BROWSABLEBAPI_NEEDED:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
    REST_FRAMEWORK['DEFAULT_PARSER_CLASSES'] = [
        'rest_framework.parsers.JSONParser',
    ]
