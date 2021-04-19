from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *

# Create your views here.
class BlogPostList(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return BlogPost.objects.all()

class BlogPostView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = 'blog'