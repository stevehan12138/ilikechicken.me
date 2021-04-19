from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogPostList.as_view(), name="blog-list"),
    path('<int:pk>/', views.BlogPostView.as_view(), name="blog-post")
]