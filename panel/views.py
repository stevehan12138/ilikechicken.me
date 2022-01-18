from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from blog.models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'panel/index.html')

def login_action(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('/panel/dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/panel/dashboard')
        return redirect('/panel/')

@login_required
def logout_action(request):
    logout(request)
    return redirect('/panel/')

@login_required
def dashboard(request):
    blog_posts = BlogPost.objects.all()
    post_num = len(blog_posts)
    username = request.user.username
    lastest_post = blog_posts.order_by('-last_edited')[0]
    print(request.path)
    return render(request, 'panel/dashboard.html', {'post_num': post_num, 'username': username, 'lastest_post': lastest_post})

@login_required
def blogs(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'panel/blogs.html', {'blog_posts': blog_posts})

@login_required
def comments(request):
    return render(request, 'panel/comments.html')

@login_required
def users(request):
    return render(request, 'panel/users.html')