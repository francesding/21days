from django.conf.urls import patterns, include, url
from django.contrib import admin
from backend_pages import (users, home)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^users$', users, name='users'),
    url(r'^$register', register, name = 'register'),
    #url(r'^admin/', include(admin.site.urls)),
)
