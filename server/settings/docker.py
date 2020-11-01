from .base import *

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "superadmin-db",
    "USER": "postgres",
    "PASSWORD": 123456,
    "HOST": "lmsdb",
    "PORT": "5432",
  }
}

ALLOWED_HOSTS = ['*']
