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
import qa.views

urlpatterns = [
    url(r'^$', http_resp_404, name='home'),
    url(r'^login/', http_resp_404, name='login'),
    url(r'^signup/', http_resp_404, name='signup'),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', http_resp_404, name='ask'),
    url(r'^popular/', http_resp_404, name='popular'),
    url(r'^new/', http_resp_404, name='new'),
    url(r'^admin/', admin.site.urls),
]
