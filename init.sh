sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/ash.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/ask/ask/wsgi.py   /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart
