from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogPostList.as_view(), name="blog-list"),
    path('<int:pk>/', views.blog_post_detail, name="blog-post")
]