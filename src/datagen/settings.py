# -----------------------------------------------------------------------------------
# Sample RapidPro settings file, this should allow you to deploy RapidPro locally on
# a PostgreSQL database.
#
# The following are requirements:
#     - a postgreSQL database named 'temba', with a user name 'temba' and
#       password 'temba' (with postgis extensions installed)
#     - a redis instance listening on localhost
# -----------------------------------------------------------------------------------
import copy
import psycopg2.extensions
import warnings

from temba.settings_common import *  # noqa

SECRET_KEY = 'klj;kljhlkjhlkjhlkjh'

DEBUG_TOOLBAR = True
DEBUG = True
from environ import Env

env = Env()
env.DB_SCHEMES['perf'] = 'datagen.db'
DATABASES = {'default': env.db()}

# DATABASES = {'default': {"ENGINE": "django.contrib.gis.db.backends.postgis",
#                          "NAME": "rapidpro",
#                          "USER": "postgres",
#                          "PASSWORD": "",
#                          "HOST": "localhost",
#                          "PORT": "5432",
#                          "ATOMIC_REQUESTS": True,
#                          "CONN_MAX_AGE": 60,
#                          "OPTIONS": {},
#                          }
#              }

# -----------------------------------------------------------------------------------
# Add a custom brand for development
# -----------------------------------------------------------------------------------

custom = copy.deepcopy(BRANDING["rapidpro.io"])
custom["name"] = "Custom Brand"
custom["slug"] = "custom"
custom["org"] = "Custom"
custom["api_link"] = "http://custom-brand.io"
custom["domain"] = "custom-brand.io"
custom["email"] = "join@custom-brand.io"
custom["support_email"] = "support@custom-brand.io"
custom["allow_signups"] = True
BRANDING["custom-brand.io"] = custom

# -----------------------------------------------------------------------------------
# Used when creating callbacks for Twilio, Nexmo etc..
# -----------------------------------------------------------------------------------
HOSTNAME = "temba.ngrok.io"
ALLOWED_HOSTS = ["*"]

# -----------------------------------------------------------------------------------
# Redis & Cache Configuration (we expect a Redis instance on localhost)
# -----------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s:%s/%s" % (REDIS_HOST, REDIS_PORT, REDIS_DB),
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

INTERNAL_IPS = ("127.0.0.1",)

# -----------------------------------------------------------------------------------
# Load development apps
# -----------------------------------------------------------------------------------
INSTALLED_APPS = INSTALLED_APPS + ("storages",)
if DEBUG_TOOLBAR:
    INSTALLED_APPS = INSTALLED_APPS + ("debug_toolbar",)

# -----------------------------------------------------------------------------------
# In development, add in extra logging for exceptions and the debug toolbar
# -----------------------------------------------------------------------------------
MIDDLEWARE = ("temba.middleware.ExceptionMiddleware",) + MIDDLEWARE
if DEBUG_TOOLBAR:
    MIDDLEWARE = ("debug_toolbar.middleware.DebugToolbarMiddleware",) + MIDDLEWARE

# -----------------------------------------------------------------------------------
# In development, perform background tasks in the web thread (synchronously)
# -----------------------------------------------------------------------------------
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_BACKEND = "memory"

# -----------------------------------------------------------------------------------
# This setting throws an exception if a naive datetime is used anywhere. (they should
# always contain a timezone)
# -----------------------------------------------------------------------------------
warnings.filterwarnings(
    "error", r"DateTimeField .* received a naive datetime", RuntimeWarning, r"django\.db\.models\.fields"
)

# -----------------------------------------------------------------------------------
# Make our sitestatic URL be our static URL on development
# -----------------------------------------------------------------------------------
STATIC_URL = "/sitestatic/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "root": {"level": "WARNING", "handlers": ["console"]},
    "formatters": {"verbose": {"format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"}},
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "verbose"},
        "null": {"class": "logging.NullHandler"},
    },
    "loggers": {
        # "pycountry": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        # "django.security.DisallowedHost": {"handlers": ["null"], "propagate": False},
        "django.db.backends": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        # "": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
        "django": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
        "temba": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
        "django.template.base": {"level": "CRITICAL", "handlers": ["null"], "propagate": False},
    },
}
