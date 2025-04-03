from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('users/', views.get_users, name='get_users'),
    path('posts/', views.get_posts, name='get_posts'),
    path('comments/', views.get_comments, name='get_comments'),
    path('likes/', views.get_likes, name='get_likes'),
    path('tags/', views.get_tags, name='get_tags'),
]