from django.conf.urls import patterns, url
from changelogs import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^login/', views.user_login, name='userlogin'),
    url(r'^logout/', views.user_logout, name='userlogout'),
    url(r'^(?P<project_name_slug>[\w\-]+)/$', views.changelog, name='changelog'),
    url(r'^(?P<project_name_slug>[\w\-]+)/addlog/$', views.addlog, name='addlog'),)

