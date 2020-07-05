#!/bin/sh
export FLASK_APP=./api/Server.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0