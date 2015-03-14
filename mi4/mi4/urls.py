from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from mi4_project import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mi4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^mi4/', include(urls)),
    url(r'^$', lambda r: HttpResponseRedirect('mi4/login')),
)
