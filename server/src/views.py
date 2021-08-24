from typing import Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate   
from .forms import NewUserForm  
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return render(request = request,template_name = 'src/home.html',context={})
    form = AuthenticationForm()
    return redirect("/login")

def logout_request(request):
    logout(request)
    messages.info(request,'Logout Succesfully!!')
    return redirect("/")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=  request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                messages.info(request,f'You are now logged in as {username}')
                return redirect("/user")   # redirect to the same page.
            else:
                messages.error(request,"Invalid username or password")
        else:        
            messages.error(request,"Invalid username or password")

    form = AuthenticationForm()
    return render(request = request , template_name = 'src/login.html',context={"form":form})

def register(request):
    # as form creates the POST request.
    if request.method == 'POST':
        form = NewUserForm(data = request.POST)
        print(dict(request.POST))
        if form.is_valid():
            user = form.save()  # user created.
            username = form.cleaned_data.get('username')
            messages.success(request,f"New Account Created : {username}")
            login(request,user)
            messages.info(request,f"You are logged in as  {username}")
            return redirect("/")    # to redirect to the homepage function from the urls.py .
        else:
            for msg in form.error_messages:     #error_messages is dictonary
                messages.error(request,f"{msg} : {form.error_messages[msg]}")

    form = NewUserForm
    return render(request = request,template_name = 'src/register.html',context={"form":form})


def SearchView(request):
    if request.method == 'POST':
        search_user = request.POST.get('search')
        results = User.objects.filter(username__contains=search_user)
        context = {
            'results':results
        }
        return render(request, 'src/search_result.html', context)
