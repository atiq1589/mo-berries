from .base import *

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "pizza-db",
    "USER": "postgres",
    "PASSWORD": 123456,
    "HOST": "db",
    "PORT": "5432",
  }
}

ALLOWED_HOSTS = ['*']
