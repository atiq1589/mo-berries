# Set up

You need **Python 3.8** installed

1. install python 3.8
1. install pipenv
1. run `pipenv install`
1. run `export DJANGO_SETTINGS_MODULE=server.settings.local-{name}` to point your settings file. Please create your own settings file. For example mine `local-atiq.py`. See demo.py in server.settings module for more details.
1. run `pipenv run ./manage.py migrate` to migrate super admin database (default)

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
  
1. run `pipenv run ./manage.py createsuperuser` to create super user
1. run `pipenv run ./manage.py runserver` to run the django dev server
1. To enbale the virtual environmnet shell run `pipenv shell` and you can run above commands without `pipenv run`
1. now open your browser and type localhost:8000 to view the site.
1. visit `localhost:8000/admin` to  view django admin. before that please create super user.

## Set Environment variable

`export DJANGO_SETTINGS_MODULE=server.settings.local-{name}`
