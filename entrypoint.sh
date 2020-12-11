#!/usr/bin/env bash
sleep 5
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 installations.wsgi --reload --workers=$WORKER_COUNT --timeout=300
