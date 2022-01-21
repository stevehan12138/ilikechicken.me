#!/bin/bash

source ~/apps/website/env/bin/activate
cd ~/apps/website/ilikechicken.me
git pull
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
touch ~/apps/website/ilikechicken.me/wsgi.py
echo done