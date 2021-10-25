from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *

# Create your views here.

def blog_post_list(request):
    blogs = BlogPost.objects.all().order_by('-last_edited')
    search = request.GET.get('q')
    if search:
        blogs = blogs.filter(title__icontains=search)
    return render(request, 'blog/index.html', {'blogs': blogs})

def blog_post_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    recent_blogs = BlogPost.objects.all().order_by('-last_edited')[:3]
    return render(request, 'blog/blog.html', {'blog': blog, 'recents': recent_blogs})