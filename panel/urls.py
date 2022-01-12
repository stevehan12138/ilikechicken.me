from django.shortcuts import render
from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index, name="auth"),
    path('login/', views.login_action, name="login-action"),
    path('logout/', views.logout_action, name="logout-action"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('blogs/', views.blogs, name="blogs"),
    path('comments/', views.comments, name="comments"),
    path('users/', views.users, name="users"),
]