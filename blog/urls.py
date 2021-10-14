from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_post_list, name="blog-list"),
    path('<int:pk>/', views.blog_post_detail, name="blog-post")
]