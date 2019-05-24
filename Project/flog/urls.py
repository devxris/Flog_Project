from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

# url for flog home page
urlpatterns = [
    # path("", views.home, name="flog-home"),           # set path with function view
    path("about/", views.about, name="flog-about"),
    path("", PostListView.as_view(), name="flog-home"),  # set path with class view
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
