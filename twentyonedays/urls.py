from django.conf.urls import patterns, include, url
from django.contrib import admin
from backend_pages import (users, home, login)#loginhandler)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^users$', users, name='users'),
    url(r'^login$', login, name='login'),
    #url(r'^loginhandler$', loginhandler, name='loginhandler'),
    #url(r'^admin/', include(admin.site.urls)),
)
