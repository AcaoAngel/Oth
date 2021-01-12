from django.urls import path
from . import views

app_name='Oth_app'
urlpatterns = [
    # path("", views.home), home moved to profiles app
    path("accounts/", views.accounts),
    path("blog/", views.blog),
    path("reports/", views.reports),
]
