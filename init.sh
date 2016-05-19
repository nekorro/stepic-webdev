#!/bin/sh

# update apps
sudo apt-get update nginx
sudo pip install --upgrade django
sudo pip install --upgrade gunicorn
