#!/bin/sh

# create db
mysql -u root -e "CREATE DATABASE IF NOT EXISTS stepic CHARACTER SET utf8;"
mysql -u root -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'django';"
mysql -u root -e "GRANT ALL PRIVILEGES ON stepic.* TO 'django'@'localhost';"
mysql -u root -e "FLUSH PRIVILEGES;"
