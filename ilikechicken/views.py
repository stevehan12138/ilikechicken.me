from django.shortcuts import render
from blog.models import BlogPost

def handler404(request, exception):
    return render(request, "page/404.html", status=404)

def home_page(request):
    blogs = BlogPost.objects.all()
    blog_count = len(blogs)
    return render(request, "page/index.html", {'blogs': blogs, 'blog_count': blog_count})