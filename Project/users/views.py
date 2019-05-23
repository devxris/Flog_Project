# built-in import
from django.shortcuts import render

# manual import
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # save valid user
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("flog-home")
    else:
        form = UserRegisterForm()  # django translate to html form
    return render(request, "users/register.html", {"form": form})
