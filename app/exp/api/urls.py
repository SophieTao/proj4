from django.conf.urls import include, url
from django.contrib import admin
from . import views 

urlpatterns = [
		url(r'^home/$', views.home,name='home'),
		url(r'^meal/(?P<meal_id>[0-9]+)/$', views.meal, name='meal'),
		url(r'^comment/(?P<comment_id>[0-9]+)/$', views.comment, name='comment'),
		url(r'^profile/(?P<profile_id>[0-9]+)/$', views.profile, name='profile'),
]
  
