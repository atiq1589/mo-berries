# Instructions

## Set up

You need **Python 3.8** installed

1. install python 3.8
1. install pipenv
1. run `pipenv install`
1. run `export DJANGO_SETTINGS_MODULE=server.settings.local-{name}` to point your settings file. Please create your own settings file. For example mine `local-atiq.py`. See demo.py in server.settings module for more details.
1. run `pipenv run ./manage.py migrate` to migrate database (default)

    ```DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": "pizza-db",
          "USER": "postgres",
          "PASSWORD": 123456,
          "HOST": "localhost",
          "PORT": "5432",
      }
    }

## How to run the application

1. run `pipenv run ./manage.py createsuperuser` to create super user _optional_
1. run `pipenv run ./manage.py runserver 0.0.0.0:80` to run the django dev server
1. or run `docker-compose up` to run the application
1. To enable the virtual environment shell run `pipenv shell` and you can run above commands without `pipenv run`
1. now open your browser and type localhost:8000 to view the site.
1. visit `localhost/admin` to  view django admin. before that please create super user.
1. visit `localhost/api/v1/` to  view API list.
1. Search: `localhost/api/v1/orders/?search=atiqul&order_status=confirmed`. Please note customer_name and customer_address are full text search. as a result you can pass customer name or customer address in `search` parameter.

## Set Environment variable

`export DJANGO_SETTINGS_MODULE=server.settings.{file_name}`
