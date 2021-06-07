from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect  
from Access.forms import UserForm  
from Access.models import User  

# Create your views here.

def home(request):

    return render(request, "Access/home.html")

def dashboard(request):

    return render(request, "Access/dashboard.html")

def search(request):

    return render(request, "Access/search.html")

def register(request):
    if request.method == "POST":  
        form = UserForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('Access/search.html')  
            except:  
                pass  
    else:  
        form = UserForm()  
    return render(request,'Access/register.html',{'form':form})  

 