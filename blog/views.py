from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView




# Create your views here.
class StartingPageView(ListView):
    """Display top 3 post order by date in index page
    """
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        """Query the posts and return 3 posts
        """
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data


# def index(request):
#     blogs = Post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/index.html", {
#         "posts" : blogs
#     })


class AllPostsView(ListView):
    """Display all posts order by date of creation latest
    """
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ['-date']
    context_object_name = "posts"


# def posts(request):
#     blogs = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "posts" : blogs
#     })


class SinglePostView(DetailView):
    """Display single post based on the slug parameter passed on url

    Returns:
        Post : The single post
        Tags : Tags related to the post
    """
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        return context




# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#        "post" : post,
#        "tags": post.tags.all()
#     })