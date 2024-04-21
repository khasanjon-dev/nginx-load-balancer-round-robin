#!/bin/sh

echo 'Waiting for postgres...'

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done

echo 'PostgreSQL started'

echo 'cd backend file'
cd /app/backend

echo 'Running migrations...'
python manage.py migrate


echo 'Collecting static files...'
python manage.py collectstatic --no-input



echo 'Running server...'
python manage.py runserver 0.0.0.0:8000


