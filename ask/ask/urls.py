"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from qa.views import *

urlpatterns = [
    url(r'^$', http_resp_200, name='root'),
    url(r'^login/', http_resp_200, name='login_root'),
    url(r'^signup/', http_resp_200, name='signup_root'),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', http_resp_200, name='ask_root'),
    url(r'^popular/', http_resp_200, name='popular_root'),
    url(r'^new/', http_resp_200, name='new_root'),
    url(r'^admin/', admin.site.urls),
]
