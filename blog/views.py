from blog.models import Post
from django.shortcuts import render
from datetime import date




# Create your views here.
def index(request):
    blogs = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html", {
        "posts" : blogs
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "posts" : blogs
    })

def post_detail(request, slug):
    post = next(post for post in blogs if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
       "post" : post
    })