import os

import dj_database_url

from .settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    "default": dj_database_url.config(env="GONDOR_DATABASE_URL"),
}

SITE_ID = 1 # set this to match your Sites setup

MEDIA_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "media")
STATIC_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "static")

# These two settings define what URLs your application knows about where
# servable files are located. Make sure the URLs used here are mapped in
# your gondor.yml under static_files.
MEDIA_URL = "/site_media/media/"
STATIC_URL = "/site_media/static/"

FILE_UPLOAD_PERMISSIONS = 0640

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django.request": {
            "propagate": True,
        },
    }
}
