#!/bin/bash
set -e

source /env/bin/activate

# $USER, $GROUP, $PROJECT_NAME, $PROJECT_TARGET_DIR and others are coming from the Dockerfile

export HOSTNAME=`cat /etc/hostname`

# Run django-admin without passing --pythonpath and --settings
export PYTHONPATH=$PROJECT_TARGET_DIR
export DJANGO_SETTINGS_MODULE=$PROJECT_NAME.settings

cd $PROJECT_TARGET_DIR

if [ "$1" == "development" ]; then
    exec django-admin runserver 0.0.0.0:$PORT
else
    exec "$@"
fi
