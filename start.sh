﻿#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn socialapex.wsgi:application --bind 0.0.0.0:$PORT
