#!/bin/bash

workon website
cd ~/ilikechicken
git pull
python manage.py migrate
python manage.py collectstatic
touch /var/www/www_ilikechicken_me_wsgi.py