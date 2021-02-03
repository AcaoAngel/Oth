from django.urls import path
from . import views


app_name='Oth_app'
urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog),
    path("reports/", views.reports),
]
