#!/bin/sh

# update apps
sudo apt-get update
sudo apt-get install nginx
sudo pip install --upgrade django
sudo pip install --upgrade gunicorn
