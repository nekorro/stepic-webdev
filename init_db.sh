#!/bin/sh

# create db
mysql -u root -e "CREATE DATABASE IF NOT EXISTS stepic_webdev CHARACTER SET utf8;"
mysql -u root -e "CREATE USER 'djangoi_app'@'localhost' IDENTIFIED BY 'django_app';"
mysql -u root -e "GRANT ALL PRIVILEGES ON stepic_webdev.* TO 'django_app'@'localhost';"
mysql -u root -e "FLUSH PRIVILEGES;"
