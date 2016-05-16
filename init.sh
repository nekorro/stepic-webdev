sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/ash.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/ash
sudo /etc/init.d/gunicorn restart