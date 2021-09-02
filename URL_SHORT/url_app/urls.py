from django.urls import path
from . import views
app_name = "url"
urlpatterns = [
    path("", views.Shortening, name="home"),
    path("u/<str:shorts>", views.Redirect, name="home")
]
