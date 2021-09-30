from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *

# Create your views here.
class BlogPostList(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return BlogPost.objects.all()

def blog_post_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    recent_blogs = BlogPost.objects.all().order_by('-last_edited')[:3]
    return render(request, 'blog/blog.html', {'blog': blog, 'recents': recent_blogs})