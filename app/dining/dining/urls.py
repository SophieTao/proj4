from django.conf.urls import include, url
from django.contrib import admin
from profiles import views as profiles_views
from cafes import views as cafes_views
from comments import views as comments_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),   
    url(r'^$', profiles_views.IndexView.as_view(), name='home'),
    url(r'^api/v1/profiles/(\d+)$', profiles_views.retrieve_profile, name='user'), 	
    url(r'^api/v1/profiles/create$', profiles_views.create_profile), 	
    
    url(r'^comment/$', comments_views.IndexView.as_view(), name='comment_list'),     
    url(r'^api/v1/comments/(\d+)$', comments_views.retrieve_comment, name='detail'),
	url(r'^api/v1/comments/(?P<pk>\d+)/edit$', comments_views.CommentUpdate.as_view(), name='comment-update'),
    url(r'^api/v1/comments/create$', comments_views.CommentCreate.as_view(), name='comment-add'),
    url(r'^api/v1/comments/(?P<pk>\d+)/delete$', comments_views.CommentDelete.as_view(), name='comment-delete'),

    url(r'^meal/$', cafes_views.IndexView.as_view(), name='cafe_list'),     
    url(r'^api/v1/meals/(\d+)$', cafes_views.retrieve_cafe, name='meal_detail'),
    url(r'^api/v1/meals/(?P<pk>\d+)/edit$', cafes_views.CafeUpdate.as_view(), name='cafe-update'),
    url(r'^api/v1/meals/create$', cafes_views.CafeCreate.as_view(), name='cafe-add'),
    url(r'^api/v1/meals/(?P<pk>\d+)/delete$', cafes_views.CafeDelete.as_view(), name='cafe-delete'),


]
