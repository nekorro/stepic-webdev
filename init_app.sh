#!/bin/sh

# configure nginx
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/ash.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
