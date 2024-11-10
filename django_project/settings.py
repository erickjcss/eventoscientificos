"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import dj_database_url

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ


""" APP_NAME = os.environ.get("FLY_APP_NAME")"""
ALLOWED_HOSTS = ["127.0.0.1"] 
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
ALLOWED_HOSTS.append('https://eventoscientificosfrontend.onrender.com')
ALLOWED_HOSTS.append('http://127.0.0.1')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'coreapi',
    'personas',
    'publications',
    'usuarios',
    'us',
    'comentarios',
    'pendientes',
    'notifica',
    'rest_framework.authtoken',
    'sesion',
    'sesi',
     'solicitud',
]

MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

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

WSGI_APPLICATION = 'django_project.wsgi.application'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


if not DEBUG:
    DATABASES = {
    'default':dj_database_url.config(
        default='postgresql://postgres:postgres@localhost/postgres',
        conn_max_age=600
    )
     #'default': {  'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3',} 
}
else:
    DATABASES = {
    'default': {  'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3',}}





REST_FRAMEWORK={
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, '/staticfiles/')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Directorio donde Django buscará archivos estáticos
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Directorio donde Django buscará archivos estáticos específicos de la aplicación
STATICFILES_DIRS = [
    BASE_DIR / 'pdfs', # Asegúrate de que 'pdfs' esté en la raíz de tu proyecto
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#CORS AUTHOTIZATION
CORS_ALLOWED_ORIGINS=["https://eventoscientificosfrontend.onrender.com","http://127.0.0.1:8000"]

CORS_ALLOW_CREDENTIALS=True

REST_FRAMEWORK={
    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema',

}