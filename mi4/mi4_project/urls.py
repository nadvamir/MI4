from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from mi4_project import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mi4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # login screen
    url(r'^login/$', views.login),

    # main screen: has messages, agents, users, and message box
    url(r'^dashboard/$', views.dashboard),

    # client info screen
    url(r'^client/(?P<client_id>\d+)/$', views.client),
    # agent bio screen
    url(r'^bio/(?P<agent_id>\d+)/$', views.bio),

    # recipient page for sending the message
    url(r'^message/(?P<agent_id>\d+)/$', views.message),
    # recipient page for updating bio
    url(r'^updbio/(?P<agent_id>\d+)/$', views.updBio),
    # recipient page for updating data on clients
    url(r'^upddata/(?P<client_id>\d+)/$', views.updData),

    # default
    url(r'^$', lambda r: HttpResponseRedirect('mi4/login')),
)
