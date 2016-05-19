#!/bin/sh

# create db
mysql -u root -e "CREATE DATABASE IF NOT EXISTS stepic CHARACTER SET utf8;"
mysql -u root -e "CREATE USER 'django_stepic'@'localhost' IDENTIFIED BY 'django_stepic';"
mysql -u root -e "GRANT ALL PRIVILEGES ON stepic.* TO 'django_stepic'@'localhost';"
mysql -u root -e "FLUSH PRIVILEGES;"
