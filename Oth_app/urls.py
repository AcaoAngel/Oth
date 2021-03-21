from django.urls import path
from . import views


app_name='Oth_app'
urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog),
    path("reports/", views.reports),
    path("data_protection/", views.data_protection, name="data_protection"),
    path("about_us/", views.about_us, name="about_us"),
]
