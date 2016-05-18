#!/bin/sh

# update apps
sudo apt-get update nginx
sudo pip install --upgrade django
sudo pip install --upgrade gunicorn

# configure nginx
sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/ash.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# create db
mysql -uroot -e "CREATE DATABASE IF NOT EXISTS stepic-webdev CHARACTER SET utf8;"
mysql -uroot -e "CREATE USER 'django' IDENTIFIED BY 'django';"
mysql -uroot -e "GRANT ALL ON stepic-webdev.* TO 'django';"
