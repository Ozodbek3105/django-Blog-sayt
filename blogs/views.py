
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
# Create your views here.


from blogs.models import Blog, Category, Comment
# from dashboard.views import users

# Create your views here.

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category=category_id,status=1)
    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category,pk=category_id)
    context = {
        "posts": posts,
        'category':category
    }
    print(f"category_id", category_id)
    return render(request, "posts_by_category.html", context)

def single_blog(request,link):
    blog = get_object_or_404(Blog,slug=link)
    if request.method == "GET":
        comments = Comment.objects.filter(blog=blog)
        comment_count = comments.count()
        context = {
            'blog':blog,
            'comments':comments,
            'comment_count':comment_count
        }
        return render(request,'single-blog.html',context)
    elif request.method == "POST":
        comment = Comment()
    
        comment.user = request.user
        comment.blog = blog
        comment.text = request.POST['comment'] 
        comment.save()
        return HttpResponseRedirect(request.path_info)

        

def search(request):
    keyword = request.GET.get('keyword','')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(body__icontains=keyword))
    context = {
        'posts':blogs,
        'keyword':keyword
    }
    print(blogs)
    return render(request,'search.html',context)