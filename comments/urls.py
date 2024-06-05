"""
User URLS configuration for the comments_project app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detailview, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
]


