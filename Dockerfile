FROM python:3.8.3

WORKDIR /var/www/source_code

COPY . /var/www/source_code

RUN pip install pipenv && \
    pipenv install 

CMD pipenv run python manage.py runserver 0.0.0.0:8000

EXPOSE 8000