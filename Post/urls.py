from django.urls import re_path
from . import views



app_name = 'Post'
urlpatterns = [
	re_path(r'^allposts$', views.all_posts , name='all_posts'),
	re_path(r'^post/(?P<id>\d+)$', views.post , name = 'post'),
	re_path(r'^post/create$', views.create_post , name='create_post'),
	re_path(r'^post/(?P<id>\d+)/edit$', views.edit_post , name = 'edit_post'),
	
	# re_path(r'^post/create$', views.create_post.as_view() , name='create_post'),
]

