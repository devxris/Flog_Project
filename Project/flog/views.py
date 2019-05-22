# built-in import
from django.shortcuts import render

# manual import
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Flog Home</h1>")


def about(request):
    return HttpResponse("<h1>About Page</h1>")
