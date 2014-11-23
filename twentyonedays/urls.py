from django.conf.urls import patterns, include, url
from django.contrib import admin
from backend_pages import (users, home, habit)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^users$', users, name='users'),
    url(r'^habit$', habit, name = 'habit'),
    #url(r'^admin/', include(admin.site.urls)),
)
