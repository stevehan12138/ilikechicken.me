from blog.views import BlogPostList
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(BlogPost)