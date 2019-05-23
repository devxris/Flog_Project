# built-in import
from django.shortcuts import render

# manual import
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # save valid user
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in!"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()  # django translate to html form
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")
