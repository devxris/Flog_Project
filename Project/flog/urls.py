from django.urls import path
from . import views

# url for flog home page
urlpatterns = [
    path("", views.home, name="flog-home"),
    path("about/", views.about, name="flog-about"),
]
