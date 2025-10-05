#!/bin/bash 
python manage.py collectstatic --noinput 
python manage.py migrate 
gunicorn socialapex.wsgi:application --bind 0.0.0.0:\$PORT 
