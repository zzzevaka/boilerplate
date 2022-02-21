import os
from pathlib import Path


def get_config_option(section, option, default=None):
    return os.environ.get("APP_{}_{}".format(section.upper(), option.upper()), default)


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = get_config_option('global', 'secret')

SITE_DOMAIN = get_config_option('global', 'site_domain', '127.0.0.1')
SITE_SCHEMA = get_config_option('global', 'site_schema', 'http')
SITE_URL = f'{SITE_SCHEMA}://{SITE_DOMAIN}'

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = '/static'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = get_config_option('media', 'AWS_ACCESS_KEY_ID', 's3_key')
AWS_SECRET_ACCESS_KEY = get_config_option('media', 'AWS_SECRET_ACCESS_KEY', 's3_secret')
AWS_STORAGE_BUCKET_NAME = get_config_option('media', 'AWS_STORAGE_BUCKET_NAME', 'media')
AWS_S3_MAX_MEMORY_SIZE = 1024 * 1024 * 32
AWS_S3_ENDPOINT_URL = get_config_option('media', 'AWS_S3_ENDPOINT_URL', 'http://minio:9000/')
AWS_S3_FILE_OVERWRITE = False
AWS_S3_SECURE_URLS = False
AWS_S3_CUSTOM_DOMAIN = f'{SITE_DOMAIN}/media'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',
]

PROJECT_APPS = [
    'utils'
]

INSTALLED_APPS += PROJECT_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'application.urls'

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
                'django.template.context_processors.csrf',
            ],
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_config_option('db', 'name'),
        'USER': get_config_option('db', 'user'),
        'PASSWORD': get_config_option('db', 'password'),
        'HOST': get_config_option('db', 'host'),
        'PORT': get_config_option('db', 'port'),
        'CONN_MAX_AGE': 0,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": get_config_option('cache', 'url'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    '--port', '8888',
    '--notebook-dir', '/notebooks',
    '--allow-root',
]
