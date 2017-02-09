"""dining URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from profiles import views as profiles_views
from cafes import views as cafes_views
from comments import views as comments_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),   
    url(r'^$', profiles_views.home, name='home'),
    url(r'^meal/$', cafes_views.meal, name='meal'),     
    url(r'^comment/$', comments_views.comment, name='comment'),     


]
