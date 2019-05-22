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

# Creating path route
# 1. include in project.urls, path(“route/“, include(“app.urls”)) (impart django.urls .include)
# 2. create app.urls.py file specify all routes paths with name and view
# 3. create http views in app.views.py file by function

# include flog urls from flog.urls, django just keep remaining string of path
# leave "" as the home page route
urlpatterns = [path("admin/", admin.site.urls), path("", include("flog.urls"))]
