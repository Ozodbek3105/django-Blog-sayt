from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from blogs.models import Blog, Category
from dashboard.forms import CategoryForm,BlogForm,AddUserForm, EditUserForm
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your views here.

# bu dekarator log in qilingan bosa korsatadi bomasa login.html ga o'tqazvoradi
@login_required(login_url='login')
def dashboard(request):
    blog_count = Blog.objects.all().count()
    category_count = Category.objects.all().count()
    context = {
        'blog_count':blog_count,
        'category_count':category_count
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    else:

        form = CategoryForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_category.html',context)



    return redirect('categories')

def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method =="GET":
        form = CategoryForm(instance=category)
        context = {
            'form':form,
            'category':category

        }
        return render(request,'dashboard/edit_category.html',context)
    
    elif request.method == "POST":
        form = CategoryForm(request.POST,instance=category )
        if form.is_valid():
            form.save()
            return redirect('categories')
        
def delete_category(request,id):
    del_category = get_object_or_404(Category,id=id)
    del_category.delete()
    return redirect('categories')

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request,'dashboard/blogs.html',context)

def add_blogs(request):
    if request.method == "GET":

        form = BlogForm()
        context = {
            'form':form
        }
        return render(request,'dashboard/add_blogs.html',context)
    elif request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            blog.slug = slugify(blog.title +""+ str(blog.id))
            blog.save()
            return redirect('blogs')
        else:
            print(form.errors)


def edit_blogs(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method =="GET":
        form = BlogForm(instance=blog)
        context = {
            'form':form,
            'blog':blog

        }
        return render(request,'dashboard/edit_blogs.html',context)
    
    elif request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs')
        else:
            print(form.errors)

def delete_blog(request,id):
    delete_blog = get_object_or_404(Blog,id=id)
    delete_blog.delete()
    return redirect("blogs")

def users(request):
    users = User.objects.all()
    context = {
        "users":users
    }
    return render(request,'dashboard/users.html',context)

def add_user(request):
    if request.method == "GET":
        form = AddUserForm()
        return render(request,'dashboard/add_user.html',{"form":form})
    
    elif request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
        else:
            print(form.errors)

def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == "GET":
        form = EditUserForm(instance=user)
        context = {
            "form":form,
            "user":user
        }
        return render(request,'dashboard/edit_user.html',context)
    elif request.method == "POST":
        form = EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)

def delete_user(request,id):
    del_user = get_object_or_404(User,id=id)
    del_user.delete()
    return redirect('users')