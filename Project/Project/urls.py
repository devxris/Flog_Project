"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# built-in import
from django.contrib import admin
from django.urls import path

# manual import
from django.urls import include
from users import views as user_views
from django.contrib.auth import views as auth_views

# Creating path route
# 1. include in project.urls, path(“route/“, include(“app.urls”)) (impart django.urls .include)
# 2. create app.urls.py file specify all routes paths with name and view
# 3. create http views in app.views.py file by function

# include flog urls from flog.urls, django just keep remaining string of path
# or use app's views directly, such as register view
# leave "" as the home page route
urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("profile/", user_views.profile, name="profile"),
    path("", include("flog.urls")),
]
