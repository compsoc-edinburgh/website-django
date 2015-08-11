#!/bin/sh
virtualenv --python=$(which python2.7) COMPSOCENV
source COMPSOCENV/bin/activate
pip install -r requirements.txt
python manage.py syncdb
python manage.py schemamigration --auto captcha
python manage.py migrate captcha
sh activate-dev-env.sh
