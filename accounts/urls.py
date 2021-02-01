from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [

    path("create_account/", views.create_account.as_view(), name='create_account'),
    path("movements_form/", views.movements_form, name='movements_form'),
    # path("view_accounts/", views.view_accounts, name='view_accounts'),
    path('view_accounts/', views.view_accounts.as_view(), name="view_accounts"),
    # path('account_detail/<int:id>/<int:id>/', views.account_detail.as_view(), name="account_detail"),#id is passed in the clicked link
    path('account_detail/<int:id>/', views.account_detail, name="account_detail"),#id is passed in the clicked link
      
]