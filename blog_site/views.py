

from django.shortcuts import redirect, render
from requests import post

from blog_site.forms import RegistrationForm
from blogs.models import Blog, Category
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import auth

def home(request):
    posts = Blog.objects.filter(is_featured=True,status=1)
    blogs = Blog.objects.filter(is_featured=False,status=1)
    # categories = Category.objects.all()
    context = {
        # 'categories':categories,
        'posts':posts,
        'blogs':blogs
    }
    return render(request, "home.html",context)
def register(request):
    if request.method == "POST":
        print(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('register')
    else:

        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request,'register.html',context)
def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form":form
        }
        return render(request,"login.html",context)
    elif request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                return redirect('login')
        return redirect('login')
    
def logout(request):
    auth.logout(request)
    return redirect('home')