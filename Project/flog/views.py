# manual import
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("<h1>Flog Home</h1>")
# def about(request):
#     return HttpResponse("<h1>About Page</h1>")
# ======================================================================

# Using templates:
# 1. create "templates" folder under flog app
# 2. create "flog" folder in "templates"
# 3. add "flog.apps.FlogConfig" to INSTALLED_APPS in Project.settings.py
# 4. add xxx.html templates
# 5. render path under templates folder(manual created)
# 6. pass data into render function with dictionary

# built-in import
from django.shortcuts import render

# Using dummy posts data ===============================================
# posts = [
#     {
#         "author": "DevXris",
#         "title": "Flog Post 1",
#         "content": "First flog post",
#         "date_posted": "May 22 2019",
#     },
#     {
#         "author": "Jone Doe",
#         "title": "Flog Post 2",
#         "content": "Second flog post",
#         "date_posted": "May 23 2019",
#     },
# ]
# def home(request):
#     context = {"posts": posts}  # pass context data into render function
#     return render(request, "flog/home.html", context)
# def about(request):
#     return render(request, "flog/about.html", {"title": "About"})
# =====================================================================


# manual import
from .models import Post


# Create your views here.
# Using Post from database ============================================
def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "flog/home.html", context)


def about(request):
    return render(request, "flog/about.html", {"title": "About"})
