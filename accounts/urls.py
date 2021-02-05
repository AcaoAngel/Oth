from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [

    path("create_account/", views.create_account, name='create_account'),
    path("movements_form/", views.movements_form, name='movements_form'),
    path("pay_form/", views.pay_form, name='pay_form'),
    path('view_accounts/', views.view_accounts.as_view(), name="view_accounts"),
    path('account_detail/<int:id>/', views.account_detail, name="account_detail"),#id is passed in the clicked link
    path('transaction_done/', views.transaction_done, name="transaction_done"),
    path('account_created/', views.account_created, name="account_created"),
      
]