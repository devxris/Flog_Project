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
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# Create your views here.
# Using Post from database ============================================
def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "flog/home.html", context)


def about(request):
    return render(request, "flog/about.html", {"title": "About"})


# Using class base views ==============================================
class PostListView(ListView):
    # assign model to Post
    model = Post
    # assign template name
    template_name = "flog/home.html"  # default for: <app>/<model>_<viewtype>.html
    # setup object to be post
    context_object_name = "posts"
    # order the post by latest one
    ordering = "-date_posted"
    # setup pagination (in url query by /?page=number)
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    # template name follows convention <app>/<model>_<viewtype>.html
    # if not assign object, in template need to use "object" directly


# inherited from LoginRequiredMixin to check if user logged in before new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]  # for "form" view
    # template follows convention <app>/<model>_<viewtype>.html but viewtype is form
    # share the same template as UpdateView

    # override form_valid() for pass in author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# inherited from UserPassesTestMixin to check the owner could update the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]  # for "form" view
    # template follows convention <app>/<model>_<viewtype>.html but viewtype is form
    # share the same template as CreateView

    # override form_valid() for pass in author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # override test_func() to check post owner
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # assign the home route after deletion is confirmed
    success_url = "/"
    # template follows convention <app>/<model>_<viewtype>.html but viewtype is confirm_delete

    # override test_func() to check post owner
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class UserPostListView(ListView):
    # assign model to Post
    model = Post
    # assign template name
    template_name = "flog/user_posts.html"  # default for: <app>/<model>_<viewtype>.html
    # setup object to be post
    context_object_name = "posts"
    # order the post by latest one
    # ordering = "-date_posted"
    # setup pagination (in url query by /?page=number)
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")
