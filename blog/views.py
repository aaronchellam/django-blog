from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.
# List view makes "post_list" available as a context object.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


# DetailView makes "post" available as a context object.
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
