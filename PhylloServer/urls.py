"""PhylloApp_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'stories/$', views.StoryList.as_view()),
    url(r'stories/new$', views.StoryNew.as_view()),
    url(r'stories/(?P<pk>[0-9]+)$', views.StoryDetail.as_view()),
    url(r'stories/(?P<longitude>^-?[0-9]\d*(\.\d+)?$)/'
        r'(?P<latitude>^-?[0-9]\d*(\.\d+)?$)/(?P<radius>[0-9]+)', views.LocationStoryList.as_view()),
    #url(r'stories/(?P<longitude>-?[1-9][0-9]*\.?[0-9]*([Ee][+-]?[0-9]+)?)/'
        #r'(?P<latitude>-?[1-9][0-9]*\.?[0-9]*([Ee][+-]?[0-9]+)?)/'
        #r'(?P<radius>[1-9][0-9]*\.?[0-9]*([Ee][+-]?[0-9]+)?)', views.LocationStoryList.as_view()),
    url(r'users/new$', views.UserNew.as_view()),
    url(r'users/login$', views.UserLogin.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)  # Not being used yet
