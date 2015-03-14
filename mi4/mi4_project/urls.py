from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from mi4_project import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mi4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # login screen
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name='auth_login'),

    # logout
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'login.html'},
        name='logout'),

    # main screen: has messages, agents, users, and message box
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # client info screen
    url(r'^client/(?P<client_id>\d+)/$', views.client, name='data'),
    # agent bio screen
    url(r'^bio/(?P<agent_id>\d+)/$', views.bio, name='bio'),

    # recipient page for updating bio
    url(r'^updbio/(?P<agent_id>\d+)/$', views.updBio, name='updbio'),

    # default
    url(r'^$', lambda r: HttpResponseRedirect('login')),
)
