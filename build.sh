#!/usr/bin/env bash
set -o errexit

pip install pipenv
pipenv install --system --deploy

python Littlelemon/manage.py collectstatic --no-input
python Littlelemon/manage.py migrate