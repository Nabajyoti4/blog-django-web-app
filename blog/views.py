from blog.models import Post
from django.shortcuts import render, get_object_or_404




# Create your views here.
def index(request):
    blogs = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html", {
        "posts" : blogs
    })

def posts(request):
    blogs = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "posts" : blogs
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
       "post" : post
    })