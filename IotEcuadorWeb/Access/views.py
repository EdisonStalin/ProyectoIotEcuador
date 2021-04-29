from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "Access/home.html")

def dashboard(request):

    return render(request, "Access/dashboard.html")

def search(request):

    return render(request, "Access/search.html")

def register(request):

    return render(request, "Access/register.html")