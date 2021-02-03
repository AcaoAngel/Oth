from django.urls import path, re_path
from . import views


app_name='profiles'
urlpatterns = [

    # re_path(r'^$', views.HomeView.as_view(), name='index'),
    re_path(r'^sign_up/$', views.SignUpView.as_view(), name='sign_up'),
    re_path(r'^sign_in/$', views.SignInView.as_view(), name='sign_in'),
    re_path(r'^sign_out/$', views.SignOutView.as_view(), name='sign_out'),
    
]