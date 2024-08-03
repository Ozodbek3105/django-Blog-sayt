

from django.shortcuts import render

from blogs.models import Blog, Category


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