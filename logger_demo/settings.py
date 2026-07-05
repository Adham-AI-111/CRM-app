from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l+x=#p7v84n!rzz&1dwvxl0u0b$459i^ht*xczww4&3isv*x=b'

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
    'base',
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

ROOT_URLCONF = 'logger_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'logger_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Default backend
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # Database file path
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# --------------------------------------
# Simple Config
# --------------------------------------

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "INFO",
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
#             "propagate": False,
#         },
#     },
# }


# ----------------------------------
# More Advance 
# ----------------------------------

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,

#     'formatters': {
#         'simple': {
#             'format': "{asctime} {levelname} {name}:{lineno} {message}",
#             'style': '{',
#         }
#     },

#     'handlers': {
#         "file": {
#             "class": "logging.handlers.TimedRotatingFileHandler",
#             "filename": "logs/app.log",
#             "when": "M",
#             "interval": 1,
#             "backupCount": 4,
#             "formatter": "simple",
#         },

#         'console':{
#             'formatter': 'simple',
#             'class': 'logging.StreamHandler',
#         }
#     },

#     'root': {
#         'handlers': ['file', 'console'],
#         'level': 'INFO',
#     }
# }


# --------------------------------
# Common For Production
# --------------------------------
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,

#     'formatters': {
#         'simple': {
#             'format': "{levelname}: {message}",
#             'style': '{',
#         },
#         'details': {
#             'format': "{asctime} {levelname} {name}:{lineno} {message}",
#             'style': '{',
#         }
#     },

#     'handlers': {
#         'app_file': {
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': BASE_DIR / "logs" / "app.log",
#             'level': 'INFO',
#             'when': 'midnight',
#             'interval': 1,
#             'backupCount': 15,
#             'formatter': 'details'
#         },
#         'error_file': {
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': BASE_DIR / "logs" / "app.log",
#             'level': 'ERROR',
#             'when': 'midnight',
#             'interval': 1,
#             'backupCount': 15,
#             'formatter': 'details'
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         }
#     },

#     'root': {
#         'handlers': ['app_file', 'error_file', 'console'],
#         'level': 'INFO',
#     },
# }


# --------------------------------
# advanced logging by using custom formatter filter
# --------------------------------

# ! in this config, i replced the default format structure with json-based format
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple': {
            'format': "{levelname}: {message}",
            'style': '{',
        },
        'json': {
            '()': "base.logging_utils.formatter_filter.JsonFormatter",
            'style': '{',
        }
    },

    'handlers': {
        'app_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': BASE_DIR / "logs" / "app.log",
            'level': 'INFO',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 15,
            'formatter': 'json'
        },
        'error_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': BASE_DIR / "logs" / "app.log",
            'level': 'ERROR',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 15,
            'formatter': 'json'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },

    'root': {
        'handlers': ['app_file', 'error_file', 'console'],
        'level': 'INFO',
    },
}



# --------------------------------
# Workflow of logging system
# --------------------------------

#   logger.info(...)
#       ↓
#   Logger
#       ↓
#   LogRecord + extra
#       ↓
#   Filter
#       ↓
#   Handler
#       ↓
#   Formatter