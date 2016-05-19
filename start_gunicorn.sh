#!/bin/sh

gunicorn -b 0.0.0.0:8080 -w 4 hello:wsgi_stepic19_app &
cd ask
gunicorn -b 0.0.0.0:8000 -w 4 ask.wsgi &
