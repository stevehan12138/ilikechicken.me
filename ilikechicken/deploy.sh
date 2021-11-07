#!/bin/bash

workon website
cd ~/ilikechicken
git pull
python manage.py migrate
python manage.py collectstatic --noinput
echo done