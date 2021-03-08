from django.urls import path, re_path , include 
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
app_name='profiles'

urlpatterns = [
    
  
    # re_path(r'^$', views.HomeView.as_view(), name='index'),
    re_path(r'sign_up/$', views.SignUpView.as_view(), name='sign_up'),
    re_path(r'^sign_in/$', views.SignInView.as_view(), name='sign_in'),
    re_path(r'^sign_out/$', views.SignOutView.as_view(), name='sign_out'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
  
    

    path('password_reset',
    auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
    name='password_reset'),

 
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done'),


    path('password_reset_confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    name='password_reset_confirm'),

    path('password-reset-complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete'),
    ]

    # path('password_reset',
    # auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset.html'),
    # name= "password_reset"),

    # path('password_change/',
    # views.PasswordChangeView.as_view(template_name = 'registration/password_change.html'),
    # name='password_change'),

    # path('password_change/done/',
    # views.PasswordChangeDoneView.as_view(template_name = 'registration/password_change_done.html'),
    # name='password_change_done'),

    # path('reset_password_complete',
    # auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'),
    # name= "password_reset_complete"), 

    # path('password_reset_confirm/<uidb64>/<token>/',
    # auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_form.html'),
    # name= "password_reset_confirm"),

    # path('password_reset/done/',
    #  auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'),
    #   name= "password_reset_done"),


    # path('password_reset_email/',
    # auth_views.PasswordResetEmailView.as_view(template_name = 'registration/password_reset_email.html'),
    # name= "password_reset_email"),


    


 
    #  1 - submit email form                         // PasswordResetView.as_view()
    #  2 - Email sent success message                // PasswordResetDoneView.as_view()
    #  3 - Link to password Reset form in email      // PasswordResetConfirmView.as_view()   
    #  4 - Password successfully changed message     // PasswordResetCompleteView.as_view()

   


   