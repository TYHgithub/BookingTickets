"""yuhuatai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from piaowu import views as piaowu_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles

urlpatterns = [

    url(r'^index_register_person/', piaowu_views.index_register_person),
    url(r'^index_register_team/', piaowu_views.index_register_team),
    url(r'^index_search_person/', piaowu_views.index_search_person),
    url(r'^index_search_team/', piaowu_views.index_search_team),
    url(r'^register_person/', piaowu_views.register_person),
    url(r'^register_team/', piaowu_views.register_team),
    url(r'^search_person/', piaowu_views.search_person),
    url(r'^search_team/', piaowu_views.search_team),

    url(r'^index/$', piaowu_views.index),
    url(r'^register/$', piaowu_views.register),
    url(r'^$', piaowu_views.index),

    url(r'^wx/$', piaowu_views.wx),
    url(r'^wx_in/$', piaowu_views.wx_in),
    url(r'^register_wx/$', piaowu_views.register_wx),
    url(r'^search_wx/$', piaowu_views.search_wx),

    url(r'^admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()