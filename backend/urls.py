from django.conf.urls import patterns, include, url
from django.contrib import admin
from backend_pages import (users, home, habit, habit_input, login, loginhandler)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^users$', users, name='users'),
    url(r'^login$', login, name='login'),
    url(r'^loginhandler$', loginhandler, name='loginhandler'),
    url(r'^habit_input$', habit_input, name = 'habit_input'),
    url(r'^habit$', habit, name = 'habit'),
    #url(r'^$register', register, name = 'register'),
    #url(r'^admin/', include(admin.site.urls)),
)
